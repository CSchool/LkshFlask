# -*- coding: utf-8 -*-

from functools import wraps

from flask import render_template


def templated(filename):
    """
    Passes view function return value as kwargs to render_template
    :param filename: template's filename
    :return: decorator
    """
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            rv = f(*args, **kwargs) or dict()
            return render_template(filename, **rv)
        return decorated
    return decorator