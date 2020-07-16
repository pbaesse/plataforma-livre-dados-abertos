#!/usr/bin/env python -*- coding: utf-8 -*-
from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextField, TextAreaField, \
    DateField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Length, \
    Email, EqualTo, Regexp
from flask_babel import _, lazy_gettext as _l
from app.models import User, Post, Software, Similar, Tag, Category, \
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
        Length(min=3)], render_kw={"placeholder": "Digite o título da fonte de dados"})
    sphere = SelectField('Esfera', choices=[('Municipal', 'Municipal'),
        ('Estadual', 'Estadual'), ('Federal', 'Federal'),
        ('Internacional','Internacional')], validators=[DataRequired()])
    description = TextAreaField(_l('Descrição'), validators=[DataRequired(),
        Length(min=0, max=150)], render_kw={"placeholder": "Digite uma breve descrição sobre a fonte de dados"})
    officialLink = StringField(_l('Link Oficial'), validators=[DataRequired('URL verificada!'),
        Regexp('^(http|https):\/\/[\w.\-]+(\.[\w.\-]+)+.*$', 0,
               'URL inválida. Use https:// no início da URL')],
               render_kw={"placeholder": "Digite a URL da fonte de dados \
(https://www.exemplo.com/)"})
    submit = SubmitField(_l('Registrar'))


class SoftwareForm(FlaskForm):
    title = StringField(_l('Título'), validators=[DataRequired()])
    license = StringField(_l('Licença'), validators=[DataRequired()])
    owner = StringField(_l('Proprietário:'), validators=[DataRequired()])
    activeDevelopment = StringField(_l('Desenvolvedor Ativo'), validators=[DataRequired(), Length(min=0, max=200)])
    downloadLink = StringField(_l('Link para Download'), validators=[DataRequired()])
    dateCreation = StringField(_l('Data de Criação'), validators=[DataRequired()])
    description = TextAreaField(_l('Descrição'), validators=[DataRequired()])
    submit = SubmitField(_l('Enviar'))


class SimilarForm(FlaskForm):
    name =  StringField(_l('Semelhante:'), id='autocomplete', validators=[DataRequired(),
        Length(min=0, max=100)], render_kw={"placeholder": "Digite o nome de um título.."})
    submit = SubmitField(_l('Registrar'))


class TagForm(FlaskForm):
    tag = StringField(_l('Palavras-Chaves'))


class CategoryForm(FlaskForm):
    category = StringField(_l('Categoria'))


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
