from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'home.views.index', name = 'home'),
    url(r'^accounts/', include('accounts.urls', namespace = 'accounts')),
    url(r'^keys/', include('keys.urls', namespace = 'keys')),
)
