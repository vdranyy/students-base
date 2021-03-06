"""studbase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	# Admin
    url(r'^admin/', include(admin.site.urls)),

	# create group
	url(r'^students/add_group', 'base.views.add_group', name='add_group'),

	# create student
	url(r'^students/(?P<group>[\w-]+)/add_student', 'base.views.add_student', name='add_student'),

	# update group
	url(r'^students/(?P<group>[\w-]+)/update_group', 'base.views.update_group', name='update_group'),
	
	# update student info
	url(r'^students/(?P<group>[\w-]+)/(?P<student>[\w-]+)/update_student', 'base.views.update_student', name='update_student'),

	# delete group
	url(r'^students/(?P<group>[\w-]+)/delete_group', 'base.views.delete_group', name='delete_group'),

	# delete student
	url(r'^student/(?P<group>[\w-]+)/(?P<student>[\w-]+)/delete_student', 'base.views.delete_student', name='delete_student'),

	# Apps
	url(r'^$', 'base.views.index', name='index'),
	url(r'^students/(?P<group>[\w-]+)/$', 'base.views.group_detail', name='group_detail'),
	url(r'^students/(?P<group>[\w-]+)/(?P<student>[\w-]+)/$', 'base.views.student_detail', name='student_detail'),

	url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'extra_context': {'next': '/'}}, name='login'), 
	url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
	url(r'accounts/register/$', 'base.views.register', name='register'),
	url(r'accounts/register/create_teacher', 'base.views.create_teacher', name='create_teacher'),

	# include AUTH
	url(r'^accounts/', include('django.contrib.auth.urls')),
]
