#!/usr/bin/env python# -*- coding: utf-8 -*-
import sys
from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app, Response
import json
from flask_login import current_user, login_required
from flask_babel import _, get_locale
from guess_language import guess_language
from app import db
from app.main.form import EditProfileForm, PostForm, SoftwareForm, \
    SimilarForm, CommentForm, ReportForm
from app.models import User, Post, Software, Similar, \
    Comment, Report
from app.main import bp

@bp.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
    g.locale = str(get_locale())

# exibição de posts e softwares
@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(page=page, per_page=1)
    softwares = Software.query.order_by(Software.timestamp.desc()).paginate(page=page, per_page=1)
    return render_template('index.html', title=(_('Página Principal')),
        posts=posts.items, softwares=softwares.items)

# page explore posts e softwares
@bp.route('/explore', methods=['GET', 'POST'])
def explore():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    softwares = Software.query.order_by(Software.timestamp.desc()).all()
    return render_template('explore.html', title=(_('Explorar')),
        posts=posts, softwares=softwares)

# Cadastrar fontes
@bp.route('/register_source', methods=['GET', 'POST'])
@login_required
def register_source():
    form = PostForm()
    if form.validate_on_submit():
        sources = Post(title=form.title.data, tag=form.tag.data,
        category=form.category.data, city=form.city.data, state=form.state.data,
        country=form.country.data, description=form.description.data,
        sphere=form.sphere.data, officialLink=form.officialLink.data,
        author=current_user)
        db.session.add(sources)
        db.session.commit()
        flash(_('Parabéns, você acabou de registrar uma fonte de dados!'))
        return redirect(url_for('main.index'))

    return render_template('register_source.html',
        title=(_('Cadastrar Fonte')), form=form)

# semelhantes
@bp.route('/_autocomplete', methods=['GET'])
def autocomplete():
    res1 = Software.query.all()
    res2 = Post.query.all()
    list_titles1 = [r.as_dict() for r in res1]
    list_titles2 = [r.as_dict() for r in res2]
    return jsonify(list_titles1 + list_titles2)

# perfil da fonte
@bp.route('/post/<title>', methods=['GET', 'POST'])
def post(title):
    post = Post.query.filter_by(title=title).first_or_404()
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    form = SimilarForm(request.form)
    if form.validate_on_submit():
        similar = Similar(name=form.name.data, post_id=post.id)
        db.session.add(similar)
        db.session.commit()
        flash(_('Você registrou uma nova opção de semelhante'))
    similares = Similar.query.filter_by(post_id=post.id).all()
    return render_template('post.html', post=post, form=form,
        similares=similares, posts=posts)

@bp.route("/deletar_similar/<int:id>")
@login_required
def deletar_similar(id):
    similar = Similar.query.filter_by(id=id).first()
    db.session.delete(similar)
    db.session.commit()
    flash(_('Semelhante foi excluído!'))
    return redirect(url_for("main.index"))

# editar a fonte
@bp.route('/edit_post/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_post(id):
    post = Post.query.get_or_404(id)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.tag = form.tag.data
        post.category = form.category.data
        post.officialLink = form.officialLink.data
        post.sphere = form.sphere.data
        post.city = form.city.data
        post.state = form.state.data
        post.country = form.country.data
        post.description = form.description.data
        db.session.add(post)
        db.session.commit()
        flash(_('Suas alterações foram salvas.'))
        return redirect(url_for('main.index'))
    form.title.data = post.title
    form.tag.data = post.tag
    form.category.data = post.category
    form.officialLink.data = post.officialLink
    form.sphere.data = post.sphere
    form.city.data = post.city
    form.state.data = post.state
    form.country.data = post.country
    form.description.data = post.description

    return render_template('edit_post.html', title=(_('Editar Fonte')),
                           form=form, post=post)

# deletar fonte
@bp.route("/deletar_post/<int:id>")
@login_required
def deletar_post(id):
    post = Post.query.filter_by(id=id).first()
    db.session.delete(post)
    db.session.commit()
    flash(_('A fonte foi excluída!'))
    return redirect(url_for("main.index"))

# Cadastrar softwares
@bp.route('/register_software', methods=['GET', 'POST'])
@login_required
def register_software():
    form = SoftwareForm()
    if form.validate_on_submit():
        software = Software(title=form.title.data, tag=form.tag.data,
        category=form.category.data, description=form.description.data,
        officialLink=form.officialLink.data, license=form.license.data,
        owner=form.owner.data, dateCreation=form.dateCreation.data,
        author=current_user)
        db.session.add(software)
        db.session.commit()
        flash(_('Parabéns, você acabou de registrar um software de dados!'))
        return redirect(url_for('main.index'))
    return render_template('register_software.html',
        title=(_('Cadastrar Software')), form=form)

# perfil do software
@bp.route('/software/<title>', methods=['GET', 'POST'])
def software(title):
    software = Software.query.filter_by(title=title).first_or_404()
    softwares = Software.query.order_by(Software.timestamp.desc()).all()

    form = SimilarForm(request.form)
    if form.validate_on_submit():
        similar = Similar(name=form.name.data, software_id=software.id)
        db.session.add(similar)
        db.session.commit()
        flash(_('Você registrou uma nova opção de semelhante'))

    similares = Similar.query.filter_by(software_id=software.id).all()

    return render_template('software.html', software=software, form=form,
        similares=similares, softwares=softwares)

# Editar software
@bp.route('/edit_software/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_software(id):
    software = Software.query.get_or_404(id)
    form = SoftwareForm()
    if form.validate_on_submit():
        software.title = form.title.data
        software.tag = form.tag.data
        software.category = form.category.data
        software.officialLink = form.officialLink.data
        software.owner = form.owner.data
        software.dateCreation = form.dateCreation.data
        software.license = form.license.data
        software.description = form.description.data
        db.session.add(software)
        db.session.commit()
        flash(_('Suas alterações foram salvas.'))
        return redirect(url_for('main.index'))
    form.title.data = software.title
    form.tag.data = software.tag
    form.category.data = software.category
    form.officialLink.data = software.officialLink
    form.owner.data = software.owner
    form.dateCreation.data = software.dateCreation
    form.license.data = software.license
    form.description.data = software.description
    return render_template('edit_software.html', title=(_('Editar Software')),
        form=form, software=software)

# deletar software
@bp.route("/deletar_software/<int:id>")
@login_required
def deletar_software(id):
    software = Software.query.filter_by(id=id).first()
    db.session.delete(software)
    db.session.commit()
    flash(_('O software foi excluído!'))
    return redirect(url_for("main.index"))

# perfil do usuário mostrando suas fontes e softwares
@bp.route('/user/<username>', methods=['GET', 'POST'])
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    posts = user.posts.order_by(Post.timestamp.desc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('main.user', title=user.username, page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.user', username=user.username, page=posts.prev_num) \
        if posts.has_prev else None
    softwares = user.softwares.order_by(Software.timestamp.desc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('main.user', title=user.username, page=softwares.next_num) \
        if softwares.has_next else None
    prev_url = url_for('main.user', username=user.username, page=softwares.prev_num) \
        if softwares.has_prev else None
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

# Deletar usuário
@bp.route("/deletar_user/<int:id>")
@login_required
def deletar_user(id):
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    flash(_('O Usuário foi excluído!'))
    return redirect(url_for("main.index"))

@bp.route('/sobre', methods=['GET', 'POST'])
def sobre():
    return render_template('sobre.html', title=(_('Sobre')))
