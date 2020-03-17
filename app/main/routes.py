from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app
from flask_login import current_user, login_required
from flask_babel import _, get_locale
from guess_language import guess_language
from app import db
from app.main.form import EditProfileForm, SourceForm, SoftwareForm
from app.models import User, Source, Software
#from app.translate import translate
from app.main import bp

@bp.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
    g.locale = str(get_locale())

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    user = {'username': 'Carol'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Principal', user=user, posts=posts)

    #registered_sources = Source.query.filter_by(user_id=current_user.id).all()
	#registered_softwares = Software.query.filter_by(user_id=current_user.id).all()
	#db.session.commit()
	#return render_template('index.html', registered_sources=registered_sources, registered_softwares=registered_softwares, title=(_('Início')))

# perfil do usuário com as suas fontes
@bp.route('/user/<username>', methods=['GET', 'POST'])
def user(username):
	user = User.query.filter_by(username=username).first_or_404()
	posts = [
		{'author': user, 'body': 'Test post #1'},
		{'author': user, 'body': 'Test post #2'}
	]
	return render_template('user.html', user=user, posts=posts)

@bp.route('/follow/<username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('index'))
    if user == current_user:
        flash('You cannot follow yourself!')
        return redirect(url_for('user', username=username))
    current_user.follow(user)
    db.session.commit()
    flash('You are following {}!'.format(username))
    return redirect(url_for('user', username=username))

@bp.route('/unfollow/<username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('index'))
    if user == current_user:
        flash('You cannot unfollow yourself!')
        return redirect(url_for('user', username=username))
    current_user.unfollow(user)
    db.session.commit()
    flash('You are not following {}.'.format(username))
    return redirect(url_for('user', username=username))

@bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
	form = EditProfileForm(current_user.username)
	if form.validate_on_submit():
		current_user.username = form.username.data
		current_user.nickname = form.nickname.data
		current_user.typeUser = form.typeUser.data
		current_user.about_me = form.about_me.data
		db.session.commit()
		flash(_('Suas alterações foram salvas.'))
		return redirect(url_for('main.edit_profile'))
	elif request.method == 'GET':
		form.username.data = current_user.username
		form.nickname.data = current_user.nickname
		form.typeUser.data = current_user.typeUser
		form.about_me.data = current_user.about_me
	return render_template('edit_profile.html', title=(_('Editar Perfil')),
                           form=form)

@bp.route('/source', methods=['GET', 'POST'])
def source():
	form = SourceForm()
	if form.validate_on_submit():
		source = Source(title=form.title.data, sphere=form.sphere.data, description=form.description.data, \
		officialLink=form.officialLink.data, datasetLink=form.datasetLink.data, user_id=current_user.id)
		db.session.add(source)
		db.session.commit()
		flash(_('Parabéns, você acabou de registrar uma fonte de dados!'))
		return redirect(url_for('main.index'))
	return render_template('source.html', title=(_('Cadastrar Fonte')), form=form)

@bp.route('/software', methods=['GET', 'POST'])
def software():
	form = SoftwareForm()
	if form.validate_on_submit():
		software = Software(title=form.title.data,description=form.description.data, \
		downloadLink=form.downloadLink.data,activeDevelopment=form.activeDevelopment.data,
						license=form.license.data, owner=form.owner.data, dateCreation=form.dateCreation.data,
						dateRelease=form.dateRelease.data, user_id=current_user.id)
		db.session.add(software)
		db.session.commit()
		flash(_('Parabéns, você acabou de registrar um software de dados!'))
		return redirect(url_for('main.index'))
	return render_template('software.html', title=(_('Cadastrar Software')), form=form)
