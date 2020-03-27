from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app
from flask_login import current_user, login_required
from flask_babel import _, get_locale
from guess_language import guess_language
from app import db
from app.main.form import EditProfileForm, PostForm, SoftwareForm, SearchForm, CommentForm
from app.models import User, Post, Software, Comment
#from app.translate import translate
from app.main import bp

# barra de pesquisa
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

# exibição de posts
@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    # fontes
    form = PostForm()
    if form.validate_on_submit():
        language = guess_language(form.post.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        post = Post(title=form.post.data, tag=form.tag.data,
            description=form.description.data, author=current_user,
            language=language)
        db.session.add(post)
        db.session.commit()
        flash(_('Your post is now live!'))
        return redirect(url_for('main.index'))

    #posts = current_user.followed_posts().all() # usuários em comum
    #posts = Post.query.order_by(Post.timestamp.desc()).all

    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('main.index', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.index', page=posts.prev_num) \
        if posts.has_prev else None

    # softwares
    form = SoftwareForm()
    if form.validate_on_submit():
        language = guess_language(form.post.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        software = Software(title=form.title.data, tag=form.tag.data,
            license=form.license.data, author=current_user, language=language)
        db.session.add(software)
        db.session.commit()
        flash(_('Your post is now live!'))
        return redirect(url_for('main.index'))

    page = request.args.get('page', 1, type=int)
    softwares = Software.query.order_by(Software.timestamp.desc()).paginate(
        page, current_app.config['SOFTWARES_PER_PAGE'], False)
    next_url = url_for('main.index', page=softwares.next_num) \
        if softwares.has_next else None
    prev_url = url_for('main.index', page=softwares.prev_num) \
        if softwares.has_prev else None

    return render_template('index.html', title=(_('Página Principal')), form=form,
            next_url=next_url, prev_url=prev_url,
            posts=posts.items, softwares=softwares.items)

# Encontre por mais fontes/softwares
@bp.route('/explore')
def explore():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('main.index', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.index', page=posts.prev_num) \
        if posts.has_prev else None

    page = request.args.get('page', 1, type=int)
    softwares = Software.query.order_by(Software.timestamp.desc()).paginate(
        page, current_app.config['SOFTWARES_PER_PAGE'], False)
    next_url = url_for('main.index', page=softwares.next_num) \
        if softwares.has_next else None
    prev_url = url_for('main.index', page=softwares.prev_num) \
        if softwares.has_prev else None

    return render_template('explore.html', title='Explore', posts=posts.items,
        softwares=softwares.items, next_url=next_url, prev_url=prev_url)

# perfil da fonte
@bp.route('/post/<title>', methods=['GET', 'POST'])
def post(title):
    post = Post.query.filter_by(title=title).first_or_404()
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('post', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('post', page=posts.prev_num) \
        if posts.has_prev else None

    form = CommentForm()
    if form.validate_on_submit():
        comments = Comment(name=name.form.data, email=email.form.data,
            comment=comment.form.data)
        db.session.add(comments)
        db.session.commit()
        flash(_('Your post is now live!'))
        return redirect(url_for('main.post'))

    return render_template('post.html', post=post, form=form,
        posts=posts.items, next_url=next_url, prev_url=prev_url)

# edite a fonte
@bp.route('/edit_post', methods=['GET', 'POST'])
@login_required
def edit_post():
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.tag = form.tag.data
        post.sphere = form.sphere.data
        post.categorie = form.categorie.data
        post.description = form.description.data
        post.officialLink = form.officialLink.data
        db.session.commit()
        flash(_('Suas alterações foram salvas.'))
        return redirect(url_for('main.edit_post'))
    return render_template('edit_post.html', title=(_('Editar Fontes')),
                           form=form)

# perfil do software
@bp.route('/software/<title>', methods=['GET', 'POST'])
def software(title):
    software = Software.query.filter_by(title=title).first_or_404()
    page = request.args.get('page', 1, type=int)
    softwares = Software.query.order_by(Software.timestamp.desc()).paginate(
        page, current_app.config['SOFTWARES_PER_PAGE'], False)
    next_url = url_for('software', page=softwares.next_num) \
        if softwares.has_next else None
    prev_url = url_for('software', page=softwares.prev_num) \
        if softwares.has_prev else None

    form = CommentForm()
    if form.validate_on_submit():
        comments = Comment(name=name.form.data, email=email.form.data,
            comment=comment.form.data)
        db.session.add(comments)
        db.session.commit()
        flash(_('Your post is now live!'))
        return redirect(url_for('main.software'))

    return render_template('software.html', software=software, form=form,
        softwares=softwares.items, next_url=next_url, prev_url=prev_url)

# Edite o software
@bp.route('/edit_software', methods=['GET', 'POST'])
def edit_software():
    form = SoftwareForm()
    if form.validate_on_submit():
        title = form.title.data
        tag = form.tag.data
        categorie = form.categorie.data
        description = form.description.data
        downloadLink = form.downloadLink.data
        activeDevelopment = form.activeDevelopment.data
        license = form.license.data
        owner = form.owner.data
        dateCreation = form.dateCreation.data
        db.session.commit()
        flash(_('Suas alterações foram salvas.'))
    return render_template('main.edit_software', title=(_('Editar Software')),
        form=form)

# perfil do usuário mostrando suas fontes e softwares
@bp.route('/user/<username>', methods=['GET', 'POST'])
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)

    posts = user.posts.order_by(Post.timestamp.desc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('user', title=user.username, page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('user', username=user.username, page=posts.prev_num) \
        if posts.has_prev else None

    softwares = user.softwares.order_by(Software.timestamp.desc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('user', title=user.username, page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('user', username=user.username, page=posts.prev_num) \
        if posts.has_prev else None

    return render_template('user.html', user=user, posts=posts.items,
        softwares=softwares.items, next_url=next_url, prev_url=prev_url)

# edite o perfil do usuário
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

# seguir usuário
@bp.route('/follow/<username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash(_('usuário {} Página não encontrada.').format(username))
        return redirect(url_for('main.index'))
    if user == current_user:
        flash(_('Você não pode seguir a si mesmo!'))
        return redirect(url_for('main.user', username=username))
    current_user.follow(user)
    db.session.commit()
    flash(_('Você está seguindo {}!').format(username))
    return redirect(url_for('main.user', username=username))

# deixar de seguir usuário
@bp.route('/unfollow/<username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash(_('Usuário {} Página não encontrada.'.format(username)))
        return redirect(url_for('main.index'))
    if user == current_user:
        flash(_('Você não pode deixar de seguir a si mesmo!'))
        return redirect(url_for('main.user', username=username))
    current_user.unfollow(user)
    db.session.commit()
    flash(_('Você não está seguindo {}.').format(username))
    return redirect(url_for('main.user', username=username))

# Cadastrar fontes
@bp.route('/register_source', methods=['GET', 'POST'])
def register_source():
	form = PostForm()
	if form.validate_on_submit():
		sources = Post(title=form.title.data, description=form.description.data, \
		      tag=form.tag.data, categorie=form.categorie.data,
              sphere=form.sphere.data, officialLink=form.officialLink.data,
              author=current_user)
		db.session.add(sources)
		db.session.commit()
		flash(_('Parabéns, você acabou de registrar uma foonte de dados!'))
		return redirect(url_for('main.index'))
	return render_template('register_source.html', title=(_('Cadastrar Fonte')), form=form)

# Cadastrar softwares
@bp.route('/register_software', methods=['GET', 'POST'])
def register_software():
	form = SoftwareForm()
	if form.validate_on_submit():
		software = Software(title=form.title.data, tag=form.tag.data, \
            categorie=form.categorie.data, description=form.description.data,
            downloadLink=form.downloadLink.data,
            activeDevelopment=form.activeDevelopment.data,
            license=form.license.data, owner=form.owner.data,
            dateCreation=form.dateCreation.data, author=current_user)
		db.session.add(software)
		db.session.commit()
		flash(_('Parabéns, você acabou de registrar um software de dados!'))
		return redirect(url_for('main.index'))
	return render_template('register_software.html', title=(_('Cadastrar Software')), form=form)
