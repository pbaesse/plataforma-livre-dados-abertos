#!/usr/bin/env python -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for, request, g
from werkzeug.urls import url_parse
from flask_babel import _, get_locale
from app import db
from app.category import bp
from app.models import Source, Software

import unicodedata
def remove_accents(category):
    try:
        category = unicode(category, 'utf-8')
    except NameError: # unicode is a default on python 3
        pass
    category = unicodedata.normalize('NFD', category)\
        .encode('ascii', 'ignore')\
        .decode("utf-8")
    return str(category.replace(" ", ""))

@bp.route('/CoronaVirus', methods=['GET', 'POST'])
def CoronaVirus():
    sources = Source.query.filter_by(category='Corona Vírus').all()
    softwares = Software.query.filter_by(category='Corona Vírus').all()
    return render_template('category/CoronaVirus.html', title=_('Corona Vírus'),
        sources=sources, softwares=softwares, remove_accents=remove_accents)

@bp.route('/Saude', methods=['GET', 'POST'])
def Saude():
    sources = Source.query.filter_by(category='Saúde').all()
    softwares = Software.query.filter_by(category='Saúde').all()
    return render_template('category/Saude.html', title=_('Saúde'),
        sources=sources, softwares=softwares, remove_accents=remove_accents)

@bp.route('/Educacao', methods=['GET', 'POST'])
def Educacao():
    sources = Source.query.filter_by(category='Educação').all()
    softwares = Software.query.filter_by(category='Educação').all()
    return render_template('category/Educacao.html', title=_('Educação'),
        sources=sources, softwares=softwares, remove_accents=remove_accents)

@bp.route('/Cinema', methods=['GET', 'POST'])
def Cinema():
    sources = Source.query.filter_by(category='Cinema').all()
    softwares = Software.query.filter_by(category='Cinema').all()
    return render_template('category/Cinema.html', title=_('Cinema'),
        sources=sources, softwares=softwares, remove_accents=remove_accents)

@bp.route('/Musica', methods=['GET', 'POST'])
def Musica():
    sources = Source.query.filter_by(category='Música').all()
    softwares = Software.query.filter_by(category='Música').all()
    return render_template('category/Musica.html', title=_('Música'),
        sources=sources, softwares=softwares, remove_accents=remove_accents)

@bp.route('/Tecnologia', methods=['GET', 'POST'])
def Tecnologia():
    sources = Source.query.filter_by(category='Tecnologia').all()
    softwares = Software.query.filter_by(category='Tecnologia').all()
    return render_template('category/Tecnologia.html', title=_('Tecnologia'),
        sources=sources, softwares=softwares, remove_accents=remove_accents)

@bp.route('/Ciencia', methods=['GET', 'POST'])
def Ciencia():
    sources = Source.query.filter_by(category='Ciência').all()
    softwares = Software.query.filter_by(category='Ciência').all()
    return render_template('category/Ciencia.html', title=_('Ciência'),
        sources=sources, softwares=softwares, remove_accents=remove_accents)

@bp.route('/SegurancaPublica', methods=['GET', 'POST'])
def SegurancaPublica():
    sources = Source.query.filter_by(category='Segurança Pública').all()
    softwares = Software.query.filter_by(category='Segurança Pública').all()
    return render_template('category/SegurancaPublica.html',
        title=_('Segurança Pública'), sources=sources, softwares=softwares)

@bp.route('/MeioAmbiente', methods=['GET', 'POST'])
def MeioAmbiente():
    sources = Source.query.filter_by(category='Meio Ambiente').all()
    softwares = Software.query.filter_by(category='Meio Ambiente').all()
    return render_template('category/MeioAmbiente.html',
        title=_('Meio Ambiente'), sources=sources, softwares=softwares,
        remove_accents=remove_accents)

@bp.route('/Cultura', methods=['GET', 'POST'])
def Cultura():
    sources = Source.query.filter_by(category='Cultura').all()
    softwares = Software.query.filter_by(category='Cultura').all()
    return render_template('category/Cultura.html', title=_('Cultura'),
        sources=sources, softwares=softwares, remove_accents=remove_accents)

@bp.route('/Paises', methods=['GET', 'POST'])
def Paises():
    sources = Source.query.filter_by(category='Países').all()
    softwares = Software.query.filter_by(category='Países').all()
    return render_template('category/Paises.html', title=_('Países'),
        sources=sources, softwares=softwares, remove_accents=remove_accents)

@bp.route('/IBGE', methods=['GET', 'POST'])
def IBGE():
    sources = Source.query.filter_by(category='IBGE').all()
    softwares = Software.query.filter_by(category='IBGE').all()
    return render_template('category/IBGE.html', title=_('IBGE'),
        softwares=softwares, sources=sources, remove_accents=remove_accents)

@bp.route('/Clima', methods=['GET', 'POST'])
def Clima():
    sources = Source.query.filter_by(category='Clima').all()
    softwares = Software.query.filter_by(category='Clima').all()
    return render_template('category/Clima.html', title=_('Clima'),
        softwares=softwares, sources=sources, remove_accents=remove_accents)

@bp.route('/Lazer', methods=['GET', 'POST'])
def Lazer():
    sources = Source.query.filter_by(category='Lazer').all()
    softwares = Software.query.filter_by(category='Lazer').all()
    return render_template('category/Lazer.html', title=_('Lazer'),
        softwares=softwares, sources=sources, remove_accents=remove_accents)
