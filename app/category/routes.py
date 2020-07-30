#!/usr/bin/env python -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for, request, g
from werkzeug.urls import url_parse
from flask_babel import _, get_locale
from app import db
from app.category import bp
from app.models import Post, Software

@bp.route('/CoronaVirus', methods=['GET', 'POST'])
def CoronaVirus():
    posts = Post.query.filter_by(category='1').all()
    softwares = Software.query.filter_by(category=1).all()
    return render_template('category/CoronaVirus.html', title=_('Corona Vírus'),
        posts=posts, softwares=softwares)

@bp.route('/Saude', methods=['GET', 'POST'])
def Saude():
    posts = Post.query.filter_by(category='Saúde').all()
    softwares = Software.query.filter_by(category='Saúde').all()
    return render_template('category/Saude.html', title=_('Saúde'),
        posts=posts, softwares=softwares)

@bp.route('/Educacao', methods=['GET', 'POST'])
def Educacao():
    posts = Post.query.filter_by(category='Educação').all()
    softwares = Software.query.filter_by(category='Educação').all()
    return render_template('category/Educacao.html', title=_('Educação'),
        posts=posts, softwares=softwares)

@bp.route('/Cinema', methods=['GET', 'POST'])
def Cinema():
    posts = Post.query.filter_by(category='Cinema').all()
    softwares = Software.query.filter_by(category='Cinema').all()
    return render_template('category/Cinema.html', title=_('Cinema'),
        posts=posts, softwares=softwares)

@bp.route('/Musica', methods=['GET', 'POST'])
def Musica():
    posts = Post.query.filter_by(category='Música').all()
    softwares = Software.query.filter_by(category='Música').all()
    return render_template('category/Musica.html', title=_('Música'),
        posts=posts, softwares=softwares)

@bp.route('/Tecnologia', methods=['GET', 'POST'])
def Tecnologia():
    posts = Post.query.filter_by(category='Tecnologia').all()
    softwares = Software.query.filter_by(category='Tecnologia').all()
    return render_template('category/Tecnologia.html', title=_('Tecnologia'),
        posts=posts, softwares=softwares)

@bp.route('/Ciencia', methods=['GET', 'POST'])
def Ciencia():
    posts = Post.query.filter_by(category='Ciência').all()
    softwares = Software.query.filter_by(category='Ciência').all()
    return render_template('category/Ciencia.html', title=_('Ciência'),
        posts=posts, softwares=softwares)

@bp.route('/SegurancaPublica', methods=['GET', 'POST'])
def SegurancaPublica():
    posts = Post.query.filter_by(category='Segurança Pública').all()
    softwares = Software.query.filter_by(category='Segurança Pública').all()
    return render_template('category/SegurancaPublica.html',
        title=_('Segurança Pública'), posts=posts, softwares=softwares)

@bp.route('/MeioAmbiente', methods=['GET', 'POST'])
def MeioAmbiente():
    posts = Post.query.filter_by(category='Meio Ambiente').all()
    softwares = Software.query.filter_by(category='Meio Ambiente').all()
    return render_template('category/MeioAmbiente.html',
        title=_('Meio Ambiente'), posts=posts, softwares=softwares)

@bp.route('/Cultura', methods=['GET', 'POST'])
def Cultura():
    posts = Post.query.filter_by(category='Cultura').all()
    softwares = Software.query.filter_by(category='Cultura').all()
    return render_template('category/Cultura.html', title=_('Cultura'),
        posts=posts, softwares=softwares)

@bp.route('/Paises', methods=['GET', 'POST'])
def Paises():
    posts = Post.query.filter_by(category='Países').all()
    softwares = Software.query.filter_by(category='Países').all()
    return render_template('category/Paises.html', title=_('Países'),
        posts=posts, softwares=softwares)

@bp.route('/IBGE', methods=['GET', 'POST'])
def IBGE():
    posts = Post.query.filter_by(category='IBGE').all()
    softwares = Software.query.filter_by(category='IBGE').all()
    return render_template('category/IBGE.html', title=_('IBGE'),
        softwares=softwares, posts=posts)

@bp.route('/Clima', methods=['GET', 'POST'])
def Clima():
    posts = Post.query.filter_by(category='Clima').all()
    softwares = Software.query.filter_by(category='Clima').all()
    return render_template('category/Clima.html', title=_('Clima'),
        softwares=softwares, posts=posts)

@bp.route('/Lazer', methods=['GET', 'POST'])
def Lazer():
    posts = Post.query.filter_by(category='Lazer').all()
    softwares = Software.query.filter_by(category='Lazer').all()
    return render_template('category/Lazer.html', title=_('Lazer'),
        softwares=softwares, posts=posts)
