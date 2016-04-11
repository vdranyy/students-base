from django import forms 
from .models import Group, Student, Teacher


class GroupForm(forms.ModelForm):
	
	class Meta:
		model = Group
		fields = ['name', 'praepostor']


class StudentForm(forms.ModelForm):
	
	class Meta:
		model = Student
		fields = ['name', 'birthday', 'student_ticket', 'student_group']


class UserForm(forms.Form):
	
	username = forms.CharField(label='Username', max_length=50, widget=forms.TextInput)
	password1 = forms.CharField(label='Password', max_length=10, min_length=6, widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirm password', max_length=10, min_length=6, widget=forms.PasswordInput)
	
	def clean_password(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError('Password didn\'t match')
		return password2


class TeacherForm(forms.ModelForm):
	
	class Meta:
		model = Teacher
		fields = ['name', 'birthday', 'teacher_id']

