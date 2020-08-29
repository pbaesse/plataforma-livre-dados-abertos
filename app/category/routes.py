#!/usr/bin/env python -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for, request, g
from werkzeug.urls import url_parse
from flask_babel import _, get_locale
from app import db
from app.category import bp
from app.models import Source, Software, Tag, Category

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

@bp.route('/CoronaVirus_Source', methods=['GET', 'POST'])
def CoronaVirus_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.tag).filter(Category.category=='Corona Vírus',
        Category.source_id == Source.id, Tag.source_id == Source.id).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/CoronaVirus_Source.html', title=(_('Corona Vírus')),
        sources=sources, remove_accents=remove_accents)

@bp.route('/CoronaVirus_Software', methods=['GET', 'POST'])
def CoronaVirus_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.tag).filter(Category.category=='Corona Vírus',
        Category.software_id == Software.id, Tag.software_id == Software.id).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/CoronaVirus_Software.html', title=(_('Corona Vírus')),
        softwares=softwares, remove_accents=remove_accents)

@bp.route('/Saude_Source', methods=['GET', 'POST'])
def Saude_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.tag).filter(Category.category=='Saúde',
        Category.source_id == Source.id, Tag.source_id == Source.id).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/Saude_Source.html', title=_('Saúde'),
        sources=sources, remove_accents=remove_accents)

@bp.route('/Saude_Software', methods=['GET', 'POST'])
def Saude_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.tag).filter(Category.category=='Saúde',
        Category.software_id == Software.id, Tag.software_id == Software.id).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/Saude_Software.html', title=_('Saúde'),
        softwares=softwares, remove_accents=remove_accents)

@bp.route('/Educacao_Source', methods=['GET', 'POST'])
def Educacao_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.tag).filter(Category.category=='Educação',
        Category.source_id == Source.id, Tag.source_id == Source.id).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/Educacao_Source.html', title=_('Educação'),
        sources=sources, remove_accents=remove_accents)

@bp.route('/Educacao_Software', methods=['GET', 'POST'])
def Educacao_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.tag).filter(Category.category=='Educação',
        Category.software_id == Software.id, Tag.software_id == Software.id).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/Educacao_Software.html', title=_('Educação'),
        softwares=softwares, remove_accents=remove_accents)

@bp.route('/Cinema_Source', methods=['GET', 'POST'])
def Cinema_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.tag).filter(Category.category=='Cinema',
        Category.source_id == Source.id, Tag.source_id == Source.id).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/Cinema_Source.html', title=_('Cinema'),
        sources=sources, remove_accents=remove_accents)

@bp.route('/Cinema_Software', methods=['GET', 'POST'])
def Cinema_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.tag).filter(Category.category=='Cinema',
        Category.software_id == Software.id, Tag.software_id == Software.id).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/Cinema_Software.html', title=_('Cinema'),
        softwares=softwares, remove_accents=remove_accents)

@bp.route('/Musica_Source', methods=['GET', 'POST'])
def Musica_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.tag).filter(Category.category=='Música',
        Category.source_id == Source.id, Tag.source_id == Source.id).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/Musica_Source.html', title=_('Música'),
        sources=sources, remove_accents=remove_accents)

@bp.route('/Musica_Software', methods=['GET', 'POST'])
def Musica_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.tag).filter(Category.category=='Música',
        Category.software_id == Software.id, Tag.software_id == Software.id).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/Musica_Software.html', title=_('Música'),
        softwares=softwares, remove_accents=remove_accents)

@bp.route('/Tecnologia_Source', methods=['GET', 'POST'])
def Tecnologia_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.tag).filter(Category.category=='Tecnologia',
        Category.source_id == Source.id, Tag.source_id == Source.id).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/Tecnologia_Source.html', title=_('Tecnologia'),
        sources=sources, remove_accents=remove_accents)

@bp.route('/Tecnologia_Software', methods=['GET', 'POST'])
def Tecnologia_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.tag).filter(Category.category=='Tecnologia',
        Category.software_id == Software.id, Tag.software_id == Software.id).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/Tecnologia_Software.html', title=_('Tecnologia'),
        softwares=softwares, remove_accents=remove_accents)

@bp.route('/Ciencia_Source', methods=['GET', 'POST'])
def Ciencia_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.tag).filter(Category.category=='Ciência',
        Category.source_id == Source.id, Tag.source_id == Source.id).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/Ciencia_Source.html', title=_('Ciência'),
        sources=sources, remove_accents=remove_accents)

@bp.route('/Ciencia_Software', methods=['GET', 'POST'])
def Ciencia_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.tag).filter(Category.category=='Ciência',
        Category.software_id == Software.id, Tag.software_id == Software.id).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/Ciencia_Software.html', title=_('Ciência'),
        softwares=softwares, remove_accents=remove_accents)

@bp.route('/SegurancaPublica_Source', methods=['GET', 'POST'])
def SegurancaPublica_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.tag).filter(Category.category=='Segurança Pública',
        Category.source_id == Source.id, Tag.source_id == Source.id).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/SegurancaPublica_Source.html',
        title=_('Segurança Pública'), sources=sources)

@bp.route('/SegurancaPublica_Software', methods=['GET', 'POST'])
def SegurancaPublica_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.tag).filter(Category.category=='Segurança Pública',
        Category.software_id == Software.id, Tag.software_id == Software.id).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/SegurancaPublica_Software.html',
        title=_('Segurança Pública'), softwares=softwares)

@bp.route('/MeioAmbiente_Source', methods=['GET', 'POST'])
def MeioAmbiente_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.tag).filter(Category.category=='Meio Ambiente',
        Category.source_id == Source.id, Tag.source_id == Source.id).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/MeioAmbiente_Source.html',
        title=_('Meio Ambiente'), sources=sources, remove_accents=remove_accents)

@bp.route('/MeioAmbiente_Software', methods=['GET', 'POST'])
def MeioAmbiente_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.tag).filter(Category.category=='Meio Ambiente',
        Category.software_id == Software.id, Tag.software_id == Software.id).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/MeioAmbiente_Software.html',
        title=_('Meio Ambiente'), softwares=softwares,
        remove_accents=remove_accents)

@bp.route('/Cultura_Source', methods=['GET', 'POST'])
def Cultura_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.tag).filter(Category.category=='Cultura',
        Category.source_id == Source.id, Tag.source_id == Source.id).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/Cultura_Source.html', title=_('Cultura'),
        sources=sources, remove_accents=remove_accents)

@bp.route('/Cultura_Software', methods=['GET', 'POST'])
def Cultura_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.tag).filter(Category.category=='Cultura',
        Category.software_id == Software.id, Tag.software_id == Software.id).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/Cultura_Software.html', title=_('Cultura'),
        softwares=softwares, remove_accents=remove_accents)

@bp.route('/Paises_Source', methods=['GET', 'POST'])
def Paises_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.tag).filter(Category.category=='Países',
        Category.source_id == Source.id, Tag.source_id == Source.id).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/Paises_Source.html', title=_('Países'),
        sources=sources, remove_accents=remove_accents)

@bp.route('/Paises_Software', methods=['GET', 'POST'])
def Paises_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.tag).filter(Category.category=='Países',
        Category.software_id == Software.id, Tag.software_id == Software.id).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/Paises_Software.html', title=_('Países'),
        softwares=softwares, remove_accents=remove_accents)

@bp.route('/IBGE_Source', methods=['GET', 'POST'])
def IBGE_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.tag).filter(Category.category=='IBGE',
        Category.source_id == Source.id, Tag.source_id == Source.id).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/IBGE_Source.html', title=_('IBGE'),
        sources=sources, remove_accents=remove_accents)

@bp.route('/IBGE_Software', methods=['GET', 'POST'])
def IBGE_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.tag).filter(Category.category=='IBGE',
        Category.software_id == Software.id, Tag.software_id == Software.id).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/IBGE_Software.html', title=_('IBGE'),
        softwares=softwares, remove_accents=remove_accents)

@bp.route('/GastosPublicos_Source', methods=['GET', 'POST'])
def GastosPublicos_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.tag).filter(Category.category=='Gastos Públicos',
        Category.source_id == Source.id, Tag.source_id == Source.id).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/GastosPublicos_Source.html', title=_('Gastos Públicos'),
        sources=sources, remove_accents=remove_accents)

@bp.route('/GastosPublicos_Software', methods=['GET', 'POST'])
def GastosPublicos_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.tag).filter(Category.category=='Gastos Públicos',
        Category.software_id == Software.id, Tag.software_id == Software.id).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/GastosPublicos_Software.html', title=_('Gastos Públicos'),
        softwares=softwares, remove_accents=remove_accents)

@bp.route('/Clima_Source', methods=['GET', 'POST'])
def Clima_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.tag).filter(Category.category=='Clima',
        Category.source_id == Source.id, Tag.source_id == Source.id).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/Clima_Source.html', title=_('Clima'),
        sources=sources, remove_accents=remove_accents)

@bp.route('/Clima_Software', methods=['GET', 'POST'])
def Clima_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.tag).filter(Category.category=='Clima',
        Category.software_id == Software.id, Tag.software_id == Software.id).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/Clima_Software.html', title=_('Clima'),
        softwares=softwares, remove_accents=remove_accents)

@bp.route('/Lazer_Source', methods=['GET', 'POST'])
def Lazer_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.tag).filter(Category.category=='Lazer',
        Category.source_id == Source.id, Tag.source_id == Source.id).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/Lazer_Source.html', title=_('Lazer'),
        sources=sources, remove_accents=remove_accents)

@bp.route('/Lazer_Software', methods=['GET', 'POST'])
def Lazer_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.tag).filter(Category.category=='Lazer',
        Category.software_id == Software.id, Tag.software_id == Software.id).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/Lazer_Software.html', title=_('Lazer'),
        softwares=softwares, remove_accents=remove_accents)
