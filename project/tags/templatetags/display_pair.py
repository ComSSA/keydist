# coding=utf-8
from __future__ import absolute_import, unicode_literals
from .nicebool import nicebool
from django import template
from django.utils.safestring import mark_safe
from django.utils.html import escape
from django.template.defaultfilters import default

register = template.Library()


@register.filter(needs_autoescape=True)
def display_pair(field, name, autoescape=None):
    if autoescape is not True:
        raise ValueError('Auto escaping must be turned on for this filter '
                         'to work')

    if field is True or field is False:
        field = nicebool(field, autoescape=True)
    else:
        field = escape(default(field, '-'))
    markup = """
    <div class='form-group'>
        <label class='col-sm-2 control-label'>{}</label>
        <div class='col-sm-10'>
            <p class='form-control-static'>{}</p>
        </div>
    </div> """.format(name, field)

    return mark_safe(markup)
