# -*- coding: utf-8 -*-

from flask import session, redirect, flash, abort
from flask_babel import gettext

from lkshflask import app, redirect_url

@app.route('/setlocale/<lang>')
def setlocale(lang):
    """
    Set current user's locale
    :param lang: language short name
    :return:
    """

    langs = app.config.get('LANGUAGES', dict())
    if lang in langs:
        session['language'] = lang
        flash(gettext("Language changed to %(lang)s", lang=langs[lang]))
        return redirect(redirect_url())
    abort(404)