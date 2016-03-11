from django.db import models


class Student(models.Model):

	name = models.CharField(max_length=80)
	birthday = models.DateField()
	student_ticket = models.IntegerField()
	student_group = models.ForeignKey('Group')
	slug = models.SlugField()

	def __unicode__(self):
		return self.name


class Group(models.Model):

	name = models.CharField(max_length=50)
	praepostor = models.ForeignKey(Student, blank=True, null=True)
	slug = models.SlugField()

	def __unicode__(self):
		return self.name
