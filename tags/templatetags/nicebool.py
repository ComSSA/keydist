from django import template
from django.utils.safestring import mark_safe
from django.utils.html import escape
from bootstrap3.templatetags.bootstrap3 import bootstrap_icon

register = template.Library()

@register.filter(needs_autoescape=True)
def nicebool(boolean, autoescape = None):
	if not autoescape:
		raise ValueError("Auto escaping must be off.")
	if boolean:
		return mark_safe(bootstrap_icon('ok'))
	else:
		return mark_safe(bootstrap_icon('remove'))