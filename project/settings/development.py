# coding=utf-8
from __future__ import absolute_import, unicode_literals
from .base import *


SECRET_KEY = '!'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
