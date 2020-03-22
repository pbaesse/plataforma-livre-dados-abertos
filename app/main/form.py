from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Length, Email, EqualTo
from flask_babel import _, lazy_gettext as _l
from app.models import User, Post, Software


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
	title = StringField(_l('Título'), validators=[DataRequired()])
	tag = StringField(_l('Tag'), validators=[DataRequired()])
	sphere = StringField(_l('Esfera'), validators=[DataRequired()])
	officialLink = StringField(_l('Link Oficial'), validators=[DataRequired()])
	description = TextAreaField(_l('Descrição'), validators=[DataRequired()])
	submit = SubmitField(_l('Enviar'))


class SoftwareForm(FlaskForm):
	title = StringField(_l('Título'), validators=[DataRequired()])
	tag = StringField(_l('Tag'), validators=[DataRequired()])
	license = StringField(_l('Licença'), validators=[DataRequired()])
	owner = StringField(_l('Proprietário'), validators=[DataRequired()])
	activeDevelopment = StringField(_l('Desenvolvedor Ativo'), validators=[DataRequired()])
	downloadLink = StringField(_l('Link para Download'), validators=[DataRequired()])
	dateCreation = StringField(_l('Data de Criação'), validators=[DataRequired()])
	description = TextAreaField(_l('Descrição'), validators=[DataRequired()])
	submit = SubmitField(_l('Enviar'))
