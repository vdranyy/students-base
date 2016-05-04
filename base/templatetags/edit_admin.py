from django import template


register = template.Library()

@register.simple_tag
def edit_object(object):
	url = '/admin/' + object._meta.app_label + '/' + object._meta.model_name + '/' + str(object.id) + '/'
	return url
