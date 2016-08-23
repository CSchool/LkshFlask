# -*- coding: utf-8 -*-

APPNAME = "lkshflask"

from flask import Flask, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel
from flask_assets import Environment

import lkshflask.config

class LkshFlaskApplication(Flask):
    "lkshflask WSGI application"

    def __str__(self):
        return "<LkshFlaskApplication>"

app = LkshFlaskApplication("lkshflask")
app.config.from_object(lkshflask.config)
db = SQLAlchemy(app)
babel = Babel(app)
assets = Environment(app)

def redirect_url(default='index'):
    """Return previous url"""
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)


import lkshflask.views
import lkshflask.models
import lkshflask.assets