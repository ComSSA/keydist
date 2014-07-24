from django import template

register = template.Library()

def name(model, plural = False):
	if plural:
		return template.defaultfilters.title(model._meta.verbose_name_plural)
	else:
		return template.defaultfilters.title(model._meta.verbose_name)

def model_name(view, plural = False):
	return name(view.model, plural)

def class_name(model, plural = False):
	return name(model.__class__, plural)


register.filter('name', name)
register.filter('model_name', model_name)
register.filter('class_name', class_name)
