# coding=utf-8
from __future__ import absolute_import, unicode_literals
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required, permission_required

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('project.accounts.urls', namespace='accounts')),
    url(r'^keys/', include('project.keys.urls', namespace='keys')),
    url(r'^policy/', include('project.policy.urls', namespace='policy')),
    url(r'^', include('project.home.urls', namespace='home')),
]
