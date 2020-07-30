#!/usr/bin/env python -*- coding: utf-8 -*-
from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextField, TextAreaField, \
    DateField, PasswordField, RadioField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Length, \
    Email, EqualTo, Regexp
from datetime import datetime
from flask_babel import _, lazy_gettext as _l
from app.models import User, Post, Software, Similar, \
    Comment, Report


class EditProfileForm(FlaskForm):
	username = StringField(_l('Nome'), validators=[DataRequired(),
        Length(min=3)], render_kw={"placeholder": "Digite um nome de usuário"})
	nickname = StringField(_l('Apelido'), validators=[DataRequired(),
        Length(min=2)], render_kw={"placeholder": "Digite seu apelido de usuário"})
	about_me = TextAreaField(_l('Sobre mim'), validators=[Length(max=150)],
        render_kw={"placeholder": "Digite uma breve descrição sobre você"})
	submit = SubmitField(_l('Salvar'))

	def __init__(self, original_username, *args, **kwargs):
		super(EditProfileForm, self).__init__(*args, **kwargs)
		self.original_username = original_username

	def validate_username(self, username):
		if username.data != self.original_username:
			user = User.query.filter_by(username=self.username.data).first()
			if user is not None:
				raise ValidationError(_('Escolha um nome diferente'))


class PostForm(FlaskForm):
    title = StringField(_l('Título'), validators=[DataRequired(),
        Length(min=3)], render_kw={"placeholder": "Digite o título da fonte de dados abertos"})
    tag = StringField(_l('Palavras-Chaves'), validators=[DataRequired()],
        render_kw={"placeholder": "Digite quais são as palavras-chaves \
(exemplo: palavra, palavra, palavra)"})
    category = SelectField(_l('Categoria'), validators=[DataRequired()],
        choices=[(1,'Corona Vírus'), (2, 'Saúde'), (3, 'Educação'),
        (4, 'Cinema'), (5, 'Música'), (6, 'Tecnologia'), (7, 'Ciência'),
        (8, 'Segurança Pública'), (9, 'Meio Ambiente'), (10, 'Cultura'),
        (11, 'Países'), (12, 'IBGE'), (12, 'Clima'), (13, 'Lazer')], default=1)
    officialLink = StringField(_l('Página Oficial'), validators=[DataRequired('URL verificada!'),
        Regexp('^(http|https):\/\/[\w.\-]+(\.[\w.\-]+)+.*$', 0,
               'URL inválida. Use https:// no início da URL')],
               render_kw={"placeholder": "Digite a URL da fonte de dados abertos \
(https://www.exemplo.com/)"})
    sphere = SelectField('Esfera', id="esfera", choices=[('Municipal', 'Municipal'),
        ('Estadual', 'Estadual'), ('Federal', 'Federal'),
        ('Internacional','Internacional')], validators=[DataRequired()])
    city = StringField(_l('Município'), id="municipal",
        render_kw={"placeholder": "Digite o Município da fonte de dados abertos"})
    state = StringField(_l('Estado'), id="estadual",
        render_kw={"placeholder": "Digite o Estato da fonte de dados abertos"})
    country = StringField(_l('País'), id="internacional",
        render_kw={"placeholder": "Digite o País da fonte de dados abertos"})
    description = TextAreaField(_l('Descrição'), validators=[DataRequired(),
        Length(min=0, max=500)], render_kw={"rows": 6, "placeholder": "Digite uma breve descrição sobre a fonte de dados abertos"})
    submit = SubmitField(_l('Registrar'))


class SoftwareForm(FlaskForm):
    title = StringField(_l('Título'), validators=[DataRequired(),
        Length(min=3)], render_kw={"placeholder": "Digite o título da aplicação"})
    tag = StringField(_l('Palavras-Chaves'), validators=[DataRequired()],
        render_kw={"placeholder": "Digite quais são as palavras-chaves \
(exemplo: palavra, palavra, palavra)"})
    category = SelectField(_l('Categoria'), validators=[DataRequired()],
        choices=[('Corona Vírus','Corona Vírus'), ('Saúde', 'Saúde'),
        ('Educação', 'Educação'), ('Cinema', 'Cinema'), ('Música', 'Música'),
        ('Tecnologia', 'Tecnologia'), ('Ciência', 'Ciência'),
        ('Segurança Pública', 'Segurança Pública'), ('Meio Ambiente', 'Meio Ambiente'),
        ('Cultura', 'Cultura'), ('Países', 'Países'), ('IBGE', 'IBGE'),
        ('Clima', 'Clima'), ('Lazer', 'Lazer')], default=1)
    officialLink = StringField(_l('Página Oficial'),
        validators=[DataRequired('URL verificada!'),
        Regexp('^(http|https):\/\/[\w.\-]+(\.[\w.\-]+)+.*$', 0,
               'URL inválida. Use https:// no início da URL')],
        render_kw={"placeholder": "Digite a URL para Página Oficial da aplicação \
(https://www.exemplo.com/)"})
    owner = StringField(_l('Proprietário/Empresa'), validators=[DataRequired(),
        Length(min=3)], render_kw={"placeholder": "Digite o nome do Proprietário/da Empresa mantedor(a) da aplicação"})
    dateCreation = DateField(_l('Data de Criação', format='%Y-%m-%d'),
        render_kw={"placeholder": "Digite a data de criação da aplicação \
(formatação: ano-mês-dia)"})
    license = SelectField('Licença', choices=[('Nenhuma', 'Nenhuma'),
        ('Apache License 2.0', 'Apache License 2.0'),
        ('GNU General Public License v3.0','GNU General Public License v3.0'),
        ('MIT License','MIT License'), ('BSD 2-Clause "Simplified" License','BSD 2-Clause "Simplified" License'),
        ('BSD 3-Clause "New" or "Revised" License','BSD 3-Clause "New" or "Revised" License'),
        ('Boost Software License 1.0','Boost Software License 1.0'),
        ('Creative Commons Zero v1.0 Universal','Creative Commons Zero v1.0 Universal'),
        ('Eclipse Public License 2.0','Eclipse Public License 2.0'),
        ('GNU Alffero General Public License v3.0','GNU Alffero General Public License v3.0'),
        ('GNU General Public License v2.0','GNU General Public License v2.0'),
        ('GNU Lesser General Public License v2.1','GNU Lesser General Public License v2.1'),
        ('Mozilla Public License 2.0','Mozilla Public License 2.0')], validators=[DataRequired()])
    description = TextAreaField(_l('Descrição'), validators=[DataRequired(),
        Length(min=0, max=500)], render_kw={"rows": 6, "placeholder": "Digite uma breve descrição sobre a aplicação"})
    submit = SubmitField(_l('Registrar'))


class SimilarForm(FlaskForm):
    name =  StringField(_l('Semelhante:'), id='autocomplete', validators=[DataRequired(),
        Length(min=0, max=100)], render_kw={"placeholder": "Digite o nome de um título.."})
    submit = SubmitField(_l('Registrar'))


class CommentForm(FlaskForm):
    name = StringField(_l('Nome'), validators=[DataRequired()])
    email = StringField(_l('E-mail'), validators=[DataRequired()])
    text = TextAreaField(_l('Comentário'), validators=[DataRequired()])
    submit = SubmitField(_l('Enviar'))


class ReportForm(FlaskForm):
    name = StringField(_l('Nome'), validators=[DataRequired()])
    description = TextAreaField(_l('Descrição'), validators=[DataRequired(),
        Length(min=0, max=150)])
    type = StringField(_l('Tipo'), validators=[DataRequired()])
    submit = SubmitField(_l('Enviar'))
