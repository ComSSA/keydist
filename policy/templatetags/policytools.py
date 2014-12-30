from django import template
from django.utils.safestring import mark_safe
from django.utils.html import escape
from tags.templatetags.nicebool import nicebool
from django.template.defaultfilters import default

register = template.Library()

@register.filter(needs_autoescape=True)
def policy_status_pretty(field, autoescape = None):
	if autoescape is not True:
		raise ValueError("Auto escaping must be turned on for this filter to work")

	if field == "In Age nda":
		color = 'primary'
	elif field == "Discussion Delayed":
		color = "info"
	elif field == "Enacted":
		color = "success"
	elif field == "Nullified":
		color = "warning"
	elif field == "Failed" or field == "Invalid":
		color = "danger"
	else:
		color = 'default'

	markup = """
	<span class="label label-%s">%s</span>
	""" % (color, field)

	return mark_safe(markup)

