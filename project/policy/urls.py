# coding=utf-8
from __future__ import absolute_import, unicode_literals
from .models import Policy, Revision, RevisionStatus
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required, permission_required
from .views import (agenda, amend, PolicyInfo, PolicyList, RevisionInfo,
                    update_status, write)

urlpatterns = [
    url(r'^$',
        permission_required('policy.read_policy')
        (PolicyList.as_view()),
        name='list'),

    url(r'^write$',
        write,
        name='write'),

    url(r'^amend/(?P<policy_id>\d+)$',
        permission_required('policy.create_revision')
        (amend),
        name='amend'),

    url(r'^(?P<pk>\d+)$',
        permission_required('policy.read_policy')
        (PolicyInfo.as_view()),
        name='info'),

    url(r'^revision/(?P<pk>\d+)$',
        permission_required('policy.read_revision')
        (RevisionInfo.as_view()),
        name='revision_info'),

    url(r'^revision/(?P<revision_id>\d+)/updatestatus$',
        permission_required('policy.create_revisionstatus')
        (update_status),
        name='update_status'),

    url(r'^agenda$',
        permission_required('policy.read_revision')
        (agenda),
        name='agenda'),
]
