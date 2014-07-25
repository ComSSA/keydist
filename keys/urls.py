from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required, permission_required

from keys import views

urlpatterns = patterns('',
    #url(r'^$',
    #	views.index,
    #	name = 'index'
    #),

    url(r'^(?P<pk>\d+)$',
        permission_required('keys.read_key')
        (views.KeyDetail.as_view()),
        name = 'detail'
    ),

    url(r'^upload$',
        permission_required('keys.create_key')
        (views.upload),
        name = 'upload'
    ),


    url(r'^product/add$',
        permission_required('keys.create_product')
        (views.ProductAdd.as_view()),
        name = 'product-add'
    ),

    url(r'^product/list$',
        permission_required('keys.read_product')
        (views.ProductList.as_view()),
        name = 'product-list'
    ),

    url(r'^product/(?P<pk>\d+)$',
        permission_required('keys.read_key')
        (views.ProductDetail.as_view()),
        name = 'product-detail'
    ),

    url(r'^product/delete/(?P<pk>\d+)$',
        permission_required('keys.delete_product')
        (views.ProductDelete.as_view()),
        name = 'product-delete'
    ),
    
    url(r'^sku/add$',
        permission_required('keys.create_sku')
        (views.SKUAdd.as_view()),
        name = 'sku-add'
    ),

    url(r'^allocate$',
        permission_required('keys.update_key')
        (views.allocate),
        name = 'allocate'
    ),


    url(r'^email/(?P<key_id>\d+)$',
        permission_required('keys.read_key')
        (views.email),
        name = 'email'
    ),
)