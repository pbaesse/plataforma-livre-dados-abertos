from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Length, Email, EqualTo
from app.models import User
from flask_babel import _, lazy_gettext as _l

class LoginForm(FlaskForm):
    username = StringField(_l('Nome'), validators=[DataRequired()])
    password = PasswordField(_l('Senha'), validators=[DataRequired()])
    remember_me = BooleanField(_l('Lembre de mim'))
    submit = SubmitField(_l('Entrar'))

class RegistrationForm(FlaskForm):
    username = StringField(_l('Nome'), validators=[DataRequired()])
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    password = PasswordField(_l('Senha'), validators=[DataRequired()])
    password2 = PasswordField(_l(
        'Repita a senha'), validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(_('Registrar'))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_('Por favor, use um nome de usuário diferente.'))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_('Por favor, use um endereço de e-mail diferente.'))

class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_l('E-mail'), validators=[DataRequired(), Email()])
    submit = SubmitField(_l('Solicitar redefinição de senha'))


class ResetPasswordForm(FlaskForm):
    password = PasswordField(_l('Senha'), validators=[DataRequired()])
    password2 = PasswordField(
        _l('Repita sua senha'), validators=[DataRequired(),
                                           EqualTo('password')])
    submit = SubmitField(_l('Solicitar redefinição de senha'))

class EditProfileForm(FlaskForm):
	username = StringField(_l('Nome'), validators=[DataRequired()])
	nickname = StringField(_l('Apelido'), validators=[DataRequired()])
	typeUser = StringField(_l('Tipo de usuário'), validators=[DataRequired()])
	about_me = TextAreaField(_l('Sobre mim'), validators=[Length(min=0, max=200)])
	submit = SubmitField(_l('Enviar'))

class SourceForm(FlaskForm):
	title = StringField(_l('Título'), validators=[DataRequired()])
	sphere = StringField(_l('Esfera'), validators=[DataRequired()])
	officialLink = StringField(_l('Link Oficial'), validators=[DataRequired()])
	datasetLink = StringField(_l('Link da Fonte de Dados'), validators=[DataRequired()])
	description = TextAreaField(_l('Descrição'), validators=[DataRequired()])
	submit = SubmitField(_l('Enviar'))

class SoftwareForm(FlaskForm):
	title = StringField(_l('Título'), validators=[DataRequired()])
	license = StringField(_l('Licença'), validators=[DataRequired()])
	owner = StringField(_l('Proprietário'), validators=[DataRequired()])
	activeDevelopment = StringField(_l('Desenvolvedor Ativo'), validators=[DataRequired()])
	downloadLink = StringField(_l('Link para Download'), validators=[DataRequired()])
	dateCreation = StringField(_l('Data de Criação'), validators=[DataRequired()])
	dateRelease	= StringField(_l('Data de Lançamento'), validators=[DataRequired()])
	description = TextAreaField(_l('Descrição'), validators=[DataRequired()])
	submit = SubmitField(_l('Enviar'))
