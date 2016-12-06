# -*- coding: utf-8 -*-

from wtforms import Form, BooleanField, TextField, PasswordField, validators


class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=6, max=24)])
    email = TextField('Email', [validators.Length(min=6, max=36)])
    password = PasswordField('New Password', [validators.Required(), validators.EqualTo('confirm', message='Password must match')])
    confirm = PasswordField("Repeart Password")
    accept_tos = BooleanField('I accept the  TOS', [validators.Required()])
