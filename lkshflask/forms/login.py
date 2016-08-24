# -*- coding: utf-8 -*-

from flask_wtf import Form
from flask_babel import gettext
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, EqualTo

from lkshflask.models.user import User
from lkshflask import db


class LoginForm(Form):
    username = StringField(gettext("Username"), validators=[DataRequired()])
    password = PasswordField(gettext("Password"), validators=[DataRequired()])
    remember_me = BooleanField(gettext("Remember me"))

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None
        self.generic_errors = []

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        user = User.query.filter(db.func.lower(User.username) == self.username.data.lower()).first()
        if user is None or not user.check_password(self.password.data):
            self.generic_errors.append(gettext("Invalid credentials"))
            return False

        self.user = user
        return True