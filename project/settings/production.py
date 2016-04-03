# coding=utf-8
from __future__ import absolute_import, unicode_literals
from .base import *
from os import environ


SECRET_KEY = environ['SECRET_KEY']

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


# Security

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_HSTS_SECONDS = 31536000  # 1 year


# Email backend

EMAIL_BACKEND = 'postmark.django_backend.EmailBackend'

POSTMARK_API_KEY = environ['POSTMARK_API_KEY']

POSTMARK_SENDER = environ['POSTMARK_SENDER']
