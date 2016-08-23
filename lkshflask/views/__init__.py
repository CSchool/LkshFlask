# -*- coding: utf-8 -*-

import pkgutil
import inspect

from flask import session, request

from lkshflask import app, babel

__all__ = []

for loader, name, is_pkg in pkgutil.walk_packages(__path__):
    module = loader.find_module(name).load_module(name)

    for name, value in inspect.getmembers(module):
        if name.startswith('__'):
            continue

        globals()[name] = value
        __all__.append(name)


@babel.localeselector
def get_locale():
    return session.get('language') or request.accept_languages.best_match(app.config.get('LANGUAGES', dict()).keys())