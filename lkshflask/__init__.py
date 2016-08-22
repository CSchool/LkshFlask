# -*- coding: utf-8 -*-

APPNAME = "lkshflask"

from flask import Flask
import lkshflask.config
from flask_sqlalchemy import SQLAlchemy

class LkshFlaskApplication(Flask):
    "lkshflask WSGI application"

    def __str__(self):
        return "<LkshFlaskApplication>"

app = LkshFlaskApplication("lkshflask")
app.config.from_object(lkshflask.config)
db = SQLAlchemy(app)

import lkshflask.views
import lkshflask.models
