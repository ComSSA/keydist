# coding=utf-8
from __future__ import absolute_import, unicode_literals
from django.core.wsgi import get_wsgi_application
"""
WSGI config for theoffice project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

application = get_wsgi_application()
