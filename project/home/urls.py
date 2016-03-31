# coding=utf-8
from __future__ import absolute_import, unicode_literals
from . import views
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required, permission_required


urlpatterns = [
    url(r'^$',
        permission_required('view_user_dashboard')
        (views.index),
        name='index'),
]
