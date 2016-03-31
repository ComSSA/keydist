# coding=utf-8
from __future__ import absolute_import, unicode_literals
from .base import *
import dj_database_url


SECRET_KEY = environ['DATABASE_SECRET_KEY']

DEBUG = False

ALLOWED_HOSTS = ['*']


# Heroku database autoconfiguration

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': environ['DATABASE_NAME'],
        'USER': environ['DATABASE_USER'],
        'PASSWORD': environ['DATABASE_PASSWORD'],
        'HOST': environ['DATABASE_HOST'],
    }
}


# Staticfiles

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
