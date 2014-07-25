from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required, permission_required

from home import views

urlpatterns = patterns('',
    url(r'^$',
        permission_required('view_user_dashboard')
    	(views.index),
    	name = 'index'
    ),
)