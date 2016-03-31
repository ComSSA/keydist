# coding=utf-8
from __future__ import absolute_import, unicode_literals
from .nicebool import nicebool
from django import template
from django.utils.safestring import mark_safe
from django.utils.html import escape
from django.template.defaultfilters import default

register = template.Library()


@register.filter
def first_item(collection):
    return collection[0]


@register.filter
def other_items(collection):
    return collection[1:]
