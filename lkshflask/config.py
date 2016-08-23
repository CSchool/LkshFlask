# -*- coding: utf-8 -*-

import os.path

WORKDIR = os.path.dirname(os.path.realpath(__file__))
SECRET_KEY = b'\nB\xd3\xa7\x9f\xd6r\x03a&R\x85\x84\xea\x0c\xab\x1eU4\x18O\xad\xda\xed'
DEBUG = True
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(WORKDIR, "lkshflask.sqlite")
SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_ENABLED = True
WTF_CSRF_SECRET_KEY = "8B92SlBhL7Hl0E4ih2l0oMHgsK2onfGgNmE89BgfPT1CyCUV98cyMXakjY0hrDuM7kPlwXE4P1eE3XRezfOg"

ASSETS_DEBUG = True

LANGUAGES = {
    "en": "English",
    "ru": "Русский"
}