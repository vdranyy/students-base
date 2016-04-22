from django.contrib import admin
from .models import Student, Group, Teacher


class StudentAdmin(admin.ModelAdmin):
#	date_hierarchy = 'birthday'
	list_display = ('name', 'birthday', 'student_group')
	list_filter = ('student_group',)
	ordering = ('name',)
	search_fields = ('name',)


class StudentInline(admin.TabularInline):
	model = Student


class GroupAdmin(admin.ModelAdmin):
	inlines = [StudentInline]
	list_display = ('name', 'praepostor')
	ordering = ('name',)
	search_fields = ('name',)


class TeacherAdmin(admin.ModelAdmin):
	list_display = ('name', 'birthday', 'teacher_id', 'user')
	ordering = ('name',)
	

admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Teacher, TeacherAdmin)

