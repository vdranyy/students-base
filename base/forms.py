from django.forms import ModelForm
from .models import Group, Student


class GroupForm(ModelForm):
	
	class Meta:
		model = Group
		fields = ['name', 'praepostor']


class StudentForm(ModelForm):
	
	class Meta:
		model = Student
		fields = ['name', 'birthday', 'student_ticket', 'student_group']
