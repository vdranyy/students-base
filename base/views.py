from django.shortcuts import render
from .models import Group


def index(request):
	context = {'groups': Group.objects.all()}
	return render(request, 'base/index.html', context)

