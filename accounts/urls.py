from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required, permission_required

from accounts import views

urlpatterns = patterns('',
    #url(r'^$', views.index, name = 'index'),
    url(r'^login/?$',
    	views.login,
    	name = 'login'
    ),
    
    url(r'^logout/?$',
    	views.logout,
    	name = 'logout'
    ),
    

    url(r'^admin$',
        permission_required('accounts.see_admin')
    	(views.admin),
    	name = 'admin'
    ),

    url(r'^admin/pass$',
        permission_required('accounts.change_user_password')
        (views.change_password_admin),
        name = 'admin-password'
    ),

    url(r'^admin/resetpass$',
        permission_required('accounts.reset_user_password')
        (views.admin_reset_password),
        name = 'admin-reset-password'
   ),

    url(r'^admin/sync$',
        permission_required('accounts.sync_permissions')
    	(views.sync),
    	name = 'permissions-sync'
    ),

    url(r'^cp$',
        login_required()
        (views.cp),
        name = 'cp',
    ),

    url(r'^cp/change_password$',
        login_required()
        (views.change_password),
        name = 'change-password',
    ),
)