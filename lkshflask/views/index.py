# -*- coding: utf-8 -*-

from lkshflask import app

@app.route('/')
def index():
    return "Hello, world"
