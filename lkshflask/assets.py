# -*- coding: utf-8 -*-

from flask_assets import Bundle

from lkshflask import assets

css = Bundle(
    'styles/main.css',
    'bower_components/bootstrap/dist/css/bootstrap.css',
    'bower_components/font-awesome/css/font-awesome.css',
    filters='cssrewrite'
)

less = Bundle(
    'styles/main.less',
    filters='less',
    output='gen/packed_less.css'
)

js = Bundle(
    'bower_components/jquery/dist/jquery.js',
    'bower_components/bootstrap/dist/js/bootstrap.js',
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