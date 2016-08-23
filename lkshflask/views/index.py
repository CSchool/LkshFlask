# -*- coding: utf-8 -*-

from lkshflask import app
from lkshflask.decorators.template import templated


@app.route('/')
@templated('base.html')
def index():
    return None
