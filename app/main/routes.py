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
from app.main.form import EditProfileForm, EditPasswordForm, \
    SourceForm, SoftwareForm, SimilarForm, CommentForm, ReportForm, ContactForm
from app.models import User, Source, Software, Similar, \
    Comment, Report
from app.main import bp

@bp.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
    g.locale = str(get_locale())

import unicodedata
def remove_accents(category):
    try:
        category = unicode(category, 'utf-8')
    except NameError: # unicode is a default on python 3
        pass
    category = unicodedata.normalize('NFD', category)\
        .encode('ascii', 'ignore')\
        .decode("utf-8")
    category.strip()
    return str(category.replace(" ", ""))

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    page = request.args.get('page', 1, type=int)
    sources = Source.query.order_by(Source.timestamp.desc()).paginate(page=page, per_page=1)
    softwares = Software.query.order_by(Software.timestamp.desc()).paginate(page=page, per_page=1)
    return render_template('index.html', title=(_('Página Principal')),
        sources=sources.items, softwares=softwares.items, remove_accents=remove_accents)

@bp.route('/explore', methods=['GET', 'POST'])
def explore():
    sources = Source.query.order_by(Source.timestamp.desc()).all()
    softwares = Software.query.order_by(Software.timestamp.desc()).all()
    return render_template('explore.html', title=(_('Fontes e Aplicações')),
        sources=sources, softwares=softwares, remove_accents=remove_accents)

@bp.route('/_autocomplete', methods=['GET'])
def autocomplete():
    res1 = Software.query.all()
    res2 = Source.query.all()
    list_titles1 = [r.as_dict() for r in res1]
    list_titles2 = [r.as_dict() for r in res2]
    return jsonify(list_titles1 + list_titles2)

@bp.route('/register_source', methods=['GET', 'POST'])
@login_required
def register_source():
    form = SourceForm()
    if form.validate_on_submit():
        sources = Source(title=form.title.data, tag=form.tag.data,
        category=form.category.data, city=form.city.data,
        state=form.state.data, country=form.country.data,
        description=form.description.data, sphere=form.sphere.data,
        officialLink=form.officialLink.data, author=current_user)
        db.session.add(sources)
        db.session.commit()
        flash(_('Você registrou uma nova Fonte de Dados Abertos'))
        return redirect(url_for('main.explore'))
    return render_template('register_source.html', title=(_('Cadastrar Fonte')),
        form=form)

@bp.route('/source/<title>', methods=['GET', 'POST'])
def source(title):
    source = Source.query.filter_by(title=title).first_or_404()
    sources = Source.query.order_by(Source.timestamp.desc()).all()
    form = SimilarForm(request.form)
    if form.validate_on_submit():
        if not current_user.is_authenticated:
            return redirect(url_for('auth.login'))
        similar = Similar(name=form.name.data, source_id=source.id)
        db.session.add(similar)
        db.session.commit()
        flash(_('Você registrou um semelhante'))
        return redirect(url_for('main.source', title=source.title))
    similares = Similar.query.filter_by(source_id=source.id).all()
    return render_template('source.html', title=(_('Perfil da Fonte')), source=source, form=form,
        similares=similares, sources=sources, remove_accents=remove_accents)

@bp.route('/edit_source/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_source(id):
    source = Source.query.get_or_404(id)
    form = SourceForm()
    if form.validate_on_submit():
        source.title = form.title.data
        source.tag = form.tag.data
        source.category = form.category.data
        source.officialLink = form.officialLink.data
        source.sphere = form.sphere.data
        source.city = form.city.data
        source.state = form.state.data
        source.country = form.country.data
        source.description = form.description.data
        db.session.add(source)
        db.session.commit()
        flash(_('As alterações foram salvas'))
        return redirect(url_for('main.source', title=source.title))
    form.title.data = source.title
    form.tag.data = source.tag
    form.category.data = source.category
    form.officialLink.data = source.officialLink
    form.sphere.data = source.sphere
    form.city.data = source.city
    form.state.data = source.state
    form.country.data = source.country
    form.description.data = source.description
    return render_template('edit_source.html', title=(_('Editar Fonte')),
                           form=form, source=source)

@bp.route("/deletar_source/<int:id>")
@login_required
def deletar_source(id):
    source = Source.query.filter_by(id=id).first()
    db.session.delete(source)
    db.session.commit()
    flash(_('A fonte foi deletada'))
    return redirect(url_for("main.explore"))

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
        flash(_('Você registrou uma nova aplicação'))
        return redirect(url_for('main.explore'))
    return render_template('register_software.html',
        title=(_('Cadastrar Aplicação')), form=form)

@bp.route('/software/<title>', methods=['GET', 'POST'])
def software(title):
    software = Software.query.filter_by(title=title).first_or_404()
    softwares = Software.query.order_by(Software.timestamp.desc()).all()
    form = SimilarForm(request.form)
    if form.validate_on_submit():
        if not current_user.is_authenticated:
            return redirect(url_for('auth.login'))
        similar = Similar(name=form.name.data, software_id=software.id)
        db.session.add(similar)
        db.session.commit()
        flash(_('Você registrou um semelhante'))
        return redirect(url_for('main.software', title=software.title))
    similares = Similar.query.filter_by(software_id=software.id).all()
    return render_template('software.html', title=(_('Perfil da Aplicação')),
        software=software, form=form, similares=similares, softwares=softwares,
        remove_accents=remove_accents)

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
        flash(_('Suas alterações foram salvas'))
        return redirect(url_for('main.software', title=software.title))
    form.title.data = software.title
    form.tag.data = software.tag
    form.category.data = software.category
    form.officialLink.data = software.officialLink
    form.owner.data = software.owner
    form.dateCreation.data = software.dateCreation
    form.license.data = software.license
    form.description.data = software.description
    return render_template('edit_software.html', title=(_('Editar Aplicação')),
        form=form, software=software)

@bp.route("/deletar_software/<int:id>")
@login_required
def deletar_software(id):
    software = Software.query.filter_by(id=id).first()
    db.session.delete(software)
    db.session.commit()
    flash(_('A aplicação foi deletada'))
    return redirect(url_for("main.explore"))

@bp.route('/user/<username>', methods=['GET', 'POST'])
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    sources = user.sources.order_by(Source.timestamp.desc()).all()
    softwares = user.softwares.order_by(Software.timestamp.desc()).all()
    return render_template('user.html', title=(_('Perfil do Usuário')),
        user=user, sources=sources, softwares=softwares,
        remove_accents=remove_accents)

@bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.nickname = form.nickname.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash(_('Suas alterações foram salvas'))
        return redirect(url_for('main.user', username=current_user.username))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.nickname.data = current_user.nickname
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title=(_('Editar Perfil')),
                           form=form)

@bp.route('/deletar_user/<int:id>')
@login_required
def deletar_user(id):
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    flash(_('O Usuário foi excluído'))
    return redirect(url_for("main.index"))

@bp.route('/edit_password', methods=["GET", "POST"])
@login_required
def edit_password():
    form = EditPasswordForm(current_user.username)
    if form.validate_on_submit():
        current_user.password_hash = form.senha
        db.session.commit()
        flash(_('Sua nova senha foi salva'))
        return redirect(url_for('main.user', username=current_user.username))
    elif request.method == 'GET':
        form.senha = current_user.password_hash
    return render_template('edit_password.html', title=(_('Editar Senha')), form=form)

@bp.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html', title=(_('Sobre')))

@bp.route('/how_to_contribute', methods=['GET', 'POST'])
def how_to_contribute():
    return render_template('how_to_contribute.html', title=(_('Como contribuir')))

@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    if current_user.is_authenticated:
        form = ContactForm(current_user.username)
        if form.validate_on_submit():
            current_user.username = form.username.data
            flash(_('Sua mensagem foi enviada'))
        elif request.method == 'GET':
            form.username.data = current_user.username
    else:
        form = ContactForm()
        if form.validate_on_submit():
            flash(_('Sua mensagem foi enviada'))
    return render_template('contact.html', title=(_('Contato')), form=form, current_user=current_user)
