from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required, permission_required

from policy import views

urlpatterns = patterns('',
    url(r'^$',
        permission_required('policy.read_policy')
        (views.PolicyList.as_view()),
        name = 'list'
    ),

    url(r'^write$',
    	views.write,
    	name = 'write'
    ),

    url(r'^amend/(?P<policy_id>\d+)$',
        permission_required('policy.create_revision')
        (views.amend),
        name = 'amend'
    ),
    
    url(r'^(?P<pk>\d+)$',
        permission_required('policy.read_policy')
        (views.PolicyInfo.as_view()),
        name = 'info'
    ),
    
    url(r'^revision/(?P<pk>\d+)$',
        permission_required('policy.read_revision')
        (views.RevisionInfo.as_view()),
        name = 'revision_info'
    ),
    
    url(r'^revision/(?P<revision_id>\d+)/updatestatus$',
        permission_required('policy.create_revisionstatus')
        (views.update_status),
        name = 'update_status'
    ),

    url(r'^agenda$',
        permission_required('policy.read_revision')
        (views.agenda),
        name = 'agenda'
    ),
)