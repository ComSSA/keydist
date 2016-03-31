# coding=utf-8
from __future__ import absolute_import, unicode_literals
from django.contrib.auth import get_user_model
from django.shortcuts import render
from keys.models import SKU


def index(request):
    return render(request, 'home/index.html', {
        'skus': SKU.objects.all(),
        'users': get_user_model().objects.all()
    })
