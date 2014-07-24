from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required, permission_required

from keys import views

urlpatterns = patterns('',
    #url(r'^$',
    #	views.index,
    #	name = 'index'
    #),

    url(r'^list$',
        permission_required('keys.read_key')
        (views.KeyList.as_view()),
        name = 'list'
    ),

    url(r'^$',
        permission_required('keys.create_key')
        (views.upload),
        name = 'upload'
    ),

    url(r'^product/add$',
        permission_required('keys.create_product')
        (views.ProductAdd.as_view()),
        name = 'product-add'
    ),

    url(r'^sku/add$',
        permission_required('keys.create_sku')
        (views.SKUAdd.as_view()),
        name = 'sku-add'
    ),
)