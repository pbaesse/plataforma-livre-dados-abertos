from flask import request
from flask_wtf import FlaskForm
from flask_wtf.html5 import URLField
from wtforms import StringField, SelectField, TextAreaField, DateField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Length, Email, EqualTo, url
from flask_babel import _, lazy_gettext as _l
from app.models import User, Post, Software


class SearchForm(FlaskForm):
    q = StringField(_l('Search'), validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        if 'formdata' not in kwargs:
            kwargs['formdata'] = request.args
        if 'csrf_enabled' not in kwargs:
            kwargs['csrf_enabled'] = False
        super(SearchForm, self).__init__(*args, **kwargs)


class EditProfileForm(FlaskForm):
	username = StringField(_l('Nome'), validators=[DataRequired()])
	nickname = StringField(_l('Apelido'), validators=[DataRequired()])
	about_me = TextAreaField(_l('Sobre mim'), validators=[Length(min=0, max=200)])
	submit = SubmitField(_l('Enviar'))

	def __init__(self, original_username, *args, **kwargs):
		super(EditProfileForm, self).__init__(*args, **kwargs)
		self.original_username = original_username

	def validate_username(self, username):
		if username.data != self.original_username:
			user = User.query.filter_by(username=self.username.data).first()
			if user is not None:
				raise ValidationError(_('Por favor digite um nome diferente.'))


class PostForm(FlaskForm):
    title = StringField(_l('Título:'), validators=[DataRequired()])
    tag = StringField(_l('Palavra-Chave:'), validators=[DataRequired()])
    sphere = SelectField('Esfera:', choices=[('Municipal', 'Municipal'),
        ('Estadual', 'Estadual'), ('Federal', 'Federal'),
        ('Internacional','Internacional')], validators=[DataRequired()])
    categorie = StringField(_l('Categoria'), validators=[DataRequired()])
    description = TextAreaField(_l('Descrição:'), validators=[DataRequired()])
    officialLink = URLField(_l('Link Oficial:'), validators=[DataRequired(), url()])
    submit = SubmitField(_l('Enviar'))


class SoftwareForm(FlaskForm):
    title = StringField(_l('Título'), validators=[DataRequired()])
    tag = StringField(_l('Palavra-Chave:'), validators=[DataRequired()])
    categorie = StringField(_l('Categoria'), validators=[DataRequired()])
    license = StringField(_l('Licença:'), validators=[DataRequired()])
    owner = StringField(_l('Proprietário:'), validators=[DataRequired()])
    activeDevelopment = StringField(_l('Desenvolvedor Ativo:'), validators=[DataRequired()])
    downloadLink = URLField(_l('Link para Download:'), validators=[DataRequired()])
    dateCreation = StringField(_l('Data de Criação:'), validators=[DataRequired()])
    description = TextAreaField(_l('Descrição'), validators=[DataRequired()])
    submit = SubmitField(_l('Enviar'))
