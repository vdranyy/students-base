from django.shortcuts import render
from .models import Group, Student


def index(request):
	context = {'groups': Group.objects.all()}
	return render(request, 'base/index.html', context)


def group_detail(request, group):
	context = {'group': Group.objects.get(slug=group)}
	return render(request, 'base/group_detail.html', context)


def student_detail(request, group, student):
	context = {'student': Group.objects.get(slug=group).student_set.filter(slug=student)[0]}
	return render(request, 'base/student_detail.html', context)

