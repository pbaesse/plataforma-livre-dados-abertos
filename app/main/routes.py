from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app
from flask_login import current_user, login_required
from flask_babel import _, get_locale
from guess_language import guess_language
from app import db
from app.main.form import EditProfileForm, PostForm, SoftwareForm, SearchForm
from app.models import User, Post, Software
#from app.translate import translate
from app.main import bp

@bp.route('/search')
def search():
    if not g.search_form.validate():
        return redirect(url_for('main.index'))
    page = request.args.get('page', 1, type=int)
    posts, total = Post.search(g.search_form.q.data, page,
                               current_app.config['POSTS_PER_PAGE'])
    next_url = url_for('main.search', q=g.search_form.q.data, page=page + 1) \
        if total > page * current_app.config['POSTS_PER_PAGE'] else None
    prev_url = url_for('main.search', q=g.search_form.q.data, page=page - 1) \
        if page > 1 else None
    return render_template('search.html', title=_('Search'), posts=posts,
                           next_url=next_url, prev_url=prev_url)

@bp.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
        g.search_form = SearchForm()
    g.locale = str(get_locale())

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, tag=form.tag.data, description=form.description.data)
        db.session.add(post)
        db.session.commit()
        flash(_('Your post is now live!'))
        return redirect(url_for('main.index'))

    page = request.args.get('page', 1, type=int)
    #posts = current_user.followed_posts().all() # usuários em comum
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False) #postagem de todos usuários
    next_url = url_for('index.html', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('index.html', page=posts.prev_num) \
        if posts.has_prev else None

    #software
    formSoftware = SoftwareForm()
    if form.validate_on_submit():
        softwares = Software(title=form.title.data, tag=form.tag.data, license=form.license.data)
        db.session.add(softwares)
        db.session.commit()
        flash(_('Your post is now live!'))
        return redirect(url_for('main.index'))

    return render_template('index.html', title=(_('Página Principal')), form=form, formSoftware=formSoftware, posts=posts.items, next_url=next_url, prev_url=prev_url)

# perfil do usuário com as suas fontes
@bp.route('/user/<username>', methods=['GET', 'POST'])
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    posts = user.posts.order_by(Post.timestamp.desc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('user', username=user.username, page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('user', username=user.username, page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('user.html', user=user, posts=posts.items, next_url=next_url, prev_url=prev_url)

@bp.route('/follow/<username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash(_('usuário {} Página não encontrada.').format(username))
        return redirect(url_for('index'))
    if user == current_user:
        flash(_('Você não pode seguir a si mesmo!'))
        return redirect(url_for('user', username=username))
    current_user.follow(user)
    db.session.commit()
    flash(_('Você está seguindo {}!').format(username))
    return redirect(url_for('user', username=username))

@bp.route('/unfollow/<username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash(_('Usuário {} Página não encontrada.'.format(username)))
        return redirect(url_for('index'))
    if user == current_user:
        flash(_('Você não pode deixar de seguir a si mesmo!'))
        return redirect(url_for('user', username=username))
    current_user.unfollow(user)
    db.session.commit()
    flash(_('Você não está seguindo {}.').format(username))
    return redirect(url_for('user', username=username))

@bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.nickname = form.nickname.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash(_('Suas alterações foram salvas.'))
        return redirect(url_for('main.edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.nickname.data = current_user.nickname
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title=(_('Editar Perfil')),
                           form=form)

@bp.route('/source', methods=['GET', 'POST'])
def source():
	form = PostForm()
	if form.validate_on_submit():
		sources = Post(title=form.title.data, description=form.description.data, \
		tag=form.tag.data, sphere=form.sphere.data, officialLink=form.officialLink.data)
		db.session.add(sources)
		db.session.commit()
		flash(_('Parabéns, você acabou de registrar uma foonte de dados!'))
		return redirect(url_for('main.index'))
	return render_template('source.html', title=(_('Cadastrar Fonte')), form=form)

@bp.route('/software', methods=['GET', 'POST'])
def software():
	form = SoftwareForm()
	if form.validate_on_submit():
		software = Software(title=form.title.data,description=form.description.data, \
		downloadLink=form.downloadLink.data,activeDevelopment=form.activeDevelopment.data,
						license=form.license.data, owner=form.owner.data, dateCreation=form.dateCreation.data)
		db.session.add(software)
		db.session.commit()
		flash(_('Parabéns, você acabou de registrar um software de dados!'))
		return redirect(url_for('main.index'))
	return render_template('software.html', title=(_('Cadastrar Software')), form=form)
