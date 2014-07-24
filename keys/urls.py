from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required, permission_required

from keys import views

urlpatterns = patterns('',
    #url(r'^$',
    #	views.index,
    #	name = 'index'
    #),

    url(r'^list$',
        views.KeyList.as_view(),
        name = 'list'
    ),

    url(r'^$',
        views.upload,
        name = 'upload'
    ),

    url(r'^product/add$',
        views.ProductAdd.as_view(),
        name = 'product-add'
    ),

    url(r'^sku/add$',
        views.SKUAdd.as_view(),
        name = 'sku-add'
    ),
)