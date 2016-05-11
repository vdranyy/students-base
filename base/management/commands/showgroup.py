from django.core.management.base import BaseCommand 
from base.models import Group, Student


class Command(BaseCommand):
	help = "This command shows list of groups and students in each group"

	def handle(self, *args, **options):
		for group in Group.objects.all():
			print "Group of %s consists of students:" % group.name
			for student in Student.objects.filter(student_group=group):
				print "---- " + student.name
