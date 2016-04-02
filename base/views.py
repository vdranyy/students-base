from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.text import slugify
from .models import Group, Student
from .forms import GroupForm, StudentForm


# base view, list of groups
def index(request):
	context = {'groups': Group.objects.all()}
	return render(request, 'base/index.html', context)


# Group detail view, list of group students
def group_detail(request, group):
	context = {'group': Group.objects.get(slug=group)}
	return render(request, 'base/group_detail.html', context)


# Student detail view, student personal info
def student_detail(request, group, student):
	context = {'student': Group.objects.get(slug=group).student_set.filter(slug=student)[0]}
	return render(request, 'base/student_detail.html', context)


# add new group
def add_group(request):
	if request.method == 'POST':
		form = GroupForm(request.POST)
		if form.is_valid():
			group_name = form.cleaned_data['name']
			group_slug = slugify(group_name)
			group = form.save(commit=False)
			group.slug = group_slug
			group.save()
			return HttpResponseRedirect('/')
	else:
		form = GroupForm()
	context = {'form': form}
	return render(request, 'base/add_group.html', context)


# add new student
def add_student(request, group):
	group = Group.objects.get(slug=group)
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			student_name = form.cleaned_data['name']
			student_slug = slugify(student_name)
			student = form.save(commit=False)
			student.slug = student_slug
			student.save()
			return HttpResponseRedirect('/')
	else:
		form = StudentForm()
	context = {'form': form, 'group': group}
	return render(request, 'base/add_student.html', context)


# delete student
def delete_student(request, group, student):
	student = Group.objects.get(slug=group).student_set.filter(slug=student)[0]
	student.delete()
	return HttpResponseRedirect('/')


# delete group
def delete_group(request, group):
	group = Group.objects.get(slug=group)
	group.delete()
	return HttpResponseRedirect('/')


# update student info
def update_student(request, group, student):
	group = Group.objects.get(slug=group)
	student = group.student_set.filter(slug=student)[0]
	form = StudentForm(request.POST or None, instance=student)
	if request.method == 'POST':
		if form.is_valid():
			student_name = form.cleaned_data['name']
			student_slug = slugify(student_name)
			student = form.save(commit=False)
			student.slug = student_slug
			student.save()
			return HttpResponseRedirect('/')
	context = {'group': group, 'student': student, 'form': form}
	return render(request, 'base/update_student.html', context)


# update group
def update_group(request, group):
	group = Group.objects.get(slug=group)
	form = GroupForm(request.POST or None, instance=group)
	if request.method == 'POST':
		if form.is_valid():
			group_name = form.cleaned_data['name']
			group_slug = slugify(group_name)
			group = form.save(commit=False)
			group.slug = group_slug
			group.save()
			return HttpResponseRedirect('/')
	context = {'group': group, 'form': form}
	return render(request, 'base/update_group.html', context)

