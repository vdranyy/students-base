from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
	name = models.CharField(max_length=80)
	birthday = models.DateField()
	student_ticket = models.IntegerField()
	student_group = models.ForeignKey('Group')
	slug = models.SlugField()

	def __unicode__(self):
		return self.name


class Group(models.Model):
	name = models.CharField(max_length=80)
	praepostor = models.ForeignKey(Student, blank=True, null=True)
	slug = models.SlugField()

	def __unicode__(self):
		return self.name


class Teacher(models.Model):
	name = models.CharField(max_length=80)
	birthday = models.DateField()
	user = models.OneToOneField(User)
	teacher_id = models.IntegerField()
	slug = models.SlugField()

	def __unicode__(self):
		return self.name

