#!/usr/bin/env python -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Length, Email, EqualTo
from app.models import User
from flask_babel import _, lazy_gettext as _l


class LoginForm(FlaskForm):
    username = StringField(_l('Nome: *'), validators=[DataRequired(),
        Length(min=3)], render_kw={"placeholder": "Digite seu nome de usuário"})
    password = PasswordField(_l('Senha: *'), validators=[DataRequired(),
        Length(min=8)], render_kw={"placeholder": "Digite sua senha \
(mínimo 8 caracteres)"})
    remember_me = BooleanField(_l('Lembrar de mim'))
    submit = SubmitField(_l('Entrar'))


class RegistrationForm(FlaskForm):
    username = StringField(_l('Nome: *'), validators=[DataRequired(),
        Length(min=3)], render_kw={"placeholder": "Digite um nome de usuário"})
    email = StringField(_l('E-mail: *'), validators=[DataRequired(), Email()],
        render_kw={"placeholder": "Digite seu endereço de e-mail"})
    senha = PasswordField(_l('Senha: *'), validators=[DataRequired(),
        Length(min=8)], render_kw={"placeholder": "Digite uma senha \
(mínimo 8 caracteres)"})
    password2 = PasswordField(_l('Repetir senha: *'), validators=[DataRequired(),
        EqualTo('senha'), Length(min=8)],
        render_kw={"placeholder": "Repita a senha anterior (mínimo 8 caracteres)"})
    submit = SubmitField(_('Inscrever'))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_('Escolha um nome de usuário diferente'))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_('Escolha um endereço de e-mail diferente'))


class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_l('E-mail: *'), validators=[DataRequired(), Email()],
        render_kw={"placeholder": "Digite o endereço de e-mail que foi cadastrado na plataforma"})
    submit = SubmitField(_l('Redefinir senha'))


class ResetPasswordForm(FlaskForm):
    password = PasswordField(_l('Senha: *'), validators=[DataRequired(),
        Length(min=8)], render_kw={"placeholder": "Digite uma senha \
(mínimo 8 caracteres)"})
    password2 = PasswordField(_l('Repetir senha: *'), validators=[DataRequired(),
        EqualTo('password'), Length(min=8)], render_kw={"placeholder":
"Repita a senha anterior (mínimo 8 caracteres)"})
    submit = SubmitField(_l('Salvar nova senha'))
