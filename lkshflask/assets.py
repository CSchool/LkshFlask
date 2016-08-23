# -*- coding: utf-8 -*-

from flask_assets import Bundle

from lkshflask import assets

css = Bundle(
    'styles/main.css',
    'libs/Bootstrap/css/bootstrap.css'
)

less = Bundle(
    'styles/main.less',
    filters='less'
)

js = Bundle(
    'libs/jQuery/jquery-3.1.0.js',
    output='gen/packed.js',
    filters='rjsmin'
)

styles = Bundle(
    css,
    less,
    output='gen/packed.css',
    filters='cssmin'
)

assets.register('styles', styles)
assets.register('javascript', js)