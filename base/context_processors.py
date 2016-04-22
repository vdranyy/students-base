from django.conf import settings


def settings_context(request):
	return {'settings': {setting : getattr(settings, setting) for setting in dir(settings)}}

