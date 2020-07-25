#!/usr/bin/env python -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for, request, g
from werkzeug.urls import url_parse
from flask_babel import _, get_locale
from app import db
from app.category import bp
from app.models import Post

@bp.route('/CoronaVirus', methods=['GET', 'POST'])
def CoronaVirus():
    page = request.args.get('page', 1, type = int)
    posts = Post.query.filter_by(category='Corona Vírus').paginate(page=page, per_page=20)
    next_url = url_for('category.CoronaVirus', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('category.CoronaVirus', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('category/CoronaVirus.html', title=_('Corona Vírus'), posts=posts, next_url=next_url, prev_url=prev_url)

@bp.route('/Saude', methods=['GET', 'POST'])
def Saude():
    page = request.args.get('page', 1, type = int)
    posts = Post.query.filter_by(category='Saúde').paginate(page=page, per_page=20)
    next_url = url_for('category.Saude', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('category.Saude', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('category/Saude.html', title=_('Saúde'), posts=posts, next_url=next_url, prev_url=prev_url)

@bp.route('/Educacao', methods=['GET', 'POST'])
def Educacao():
    page = request.args.get('page', 1, type = int)
    posts = Post.query.filter_by(category='Educação').paginate(page=page, per_page=20)
    next_url = url_for('category.Educacao', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('category.Educacao', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('category/Educacao.html', title=_('Educação'), posts=posts, next_url=next_url, prev_url=prev_url)

@bp.route('/Cinema', methods=['GET', 'POST'])
def Cinema():
    page = request.args.get('page', 1, type = int)
    posts = Post.query.filter_by(category='Cinema').paginate(page=page, per_page=20)
    next_url = url_for('category.Cinema', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('category.Cinema', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('category/Cinema.html', title=_('Cinema'), posts=posts, next_url=next_url, prev_url=prev_url)

@bp.route('/Musica', methods=['GET', 'POST'])
def Musica():
    page = request.args.get('page', 1, type = int)
    posts = Post.query.filter_by(category='Música').paginate(page=page, per_page=20)
    next_url = url_for('category.Musica', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('category.Musica', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('category/Musica.html', title=_('Música'), posts=posts, next_url=next_url, prev_url=prev_url)

@bp.route('/Tecnologia', methods=['GET', 'POST'])
def Tecnologia():
    page = request.args.get('page', 1, type = int)
    posts = Post.query.filter_by(category='Tecnologia').paginate(page=page, per_page=20)
    next_url = url_for('category.Tecnologia', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('category.Tecnologia', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('category/Tecnologia.html', title=_('Tecnologia'), posts=posts, next_url=next_url, prev_url=prev_url)

@bp.route('/Ciencia', methods=['GET', 'POST'])
def Ciencia():
    page = request.args.get('page', 1, type = int)
    posts = Post.query.filter_by(category='Ciência').paginate(page=page, per_page=20)
    next_url = url_for('category.Ciencia', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('category.Ciencia', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('category/Ciencia.html', title=_('Ciência'), posts=posts, next_url=next_url, prev_url=prev_url)

@bp.route('/SegurancaPublica', methods=['GET', 'POST'])
def SegurancaPublica():
    page = request.args.get('page', 1, type = int)
    posts = Post.query.filter_by(category='Segurança Pública').paginate(page=page, per_page=20)
    next_url = url_for('category.SegurancaPublica', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('category.SegurancaPublica', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('category/SegurancaPublica.html', title=_('Segurança Pública'), posts=posts, next_url=next_url, prev_url=prev_url)

@bp.route('/MeioAmbiente', methods=['GET', 'POST'])
def MeioAmbiente():
    page = request.args.get('page', 1, type = int)
    posts = Post.query.filter_by(category='Meio Ambiente').paginate(page=page, per_page=20)
    next_url = url_for('category.MeioAmbiente', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('category.MeioAmbiente', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('category/MeioAmbiente.html', title=_('Meio Ambiente'), posts=posts, next_url=next_url, prev_url=prev_url)

@bp.route('/Cultura', methods=['GET', 'POST'])
def Cultura():
    page = request.args.get('page', 1, type = int)
    posts = Post.query.filter_by(category='Cultura').paginate(page=page, per_page=20)
    next_url = url_for('category.Cultura', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('category.Cultura', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('category/Cultura.html', title=_('Cultura'), posts=posts, next_url=next_url, prev_url=prev_url)

@bp.route('/Paises', methods=['GET', 'POST'])
def Paises():
    page = request.args.get('page', 1, type = int)
    posts = Post.query.filter_by(category='Países').paginate(page=page, per_page=20)
    next_url = url_for('category.Paises', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('category.Paises', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('category/Paises.html', title=_('Países'), posts=posts, next_url=next_url, prev_url=prev_url)

@bp.route('/IBGE', methods=['GET', 'POST'])
def IBGE():
    page = request.args.get('page', 1, type = int)
    posts = Post.query.filter_by(category='IBGE').paginate(page=page, per_page=20)
    next_url = url_for('category.IBGE', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('category.IBGE', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('category/IBGE.html', title=_('IBGE'), posts=posts, next_url=next_url, prev_url=prev_url)

@bp.route('/Clima', methods=['GET', 'POST'])
def Clima():
    page = request.args.get('page', 1, type = int)
    posts = Post.query.filter_by(category='Clima').paginate(page=page, per_page=20)
    next_url = url_for('category.Clima', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('category.Clima', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('category/Clima.html', title=_('Clima'), posts=posts, next_url=next_url, prev_url=prev_url)
