# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, request, flash, redirect
from flask_login import login_user
from flask_babel import gettext

from lkshflask import app, redirect_url
from lkshflask.forms.login import LoginForm

mod = Blueprint('users', __name__, url_prefix='/user')


@mod.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        login_user(form.user, remember=form.remember_me.data)
        flash(gettext('Welcome back, %(user)s'))
        return redirect(redirect_url())
    return render_template("users/login.html", form=form)


app.register_blueprint(mod)
