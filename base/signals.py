from datetime import datetime
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Group, Student, Teacher, History


@receiver(post_save, sender=Group)
@receiver(post_save, sender=Student)
@receiver(post_save, sender=Teacher)
@receiver(post_delete, sender=Group)
@receiver(post_delete, sender=Student)
@receiver(post_delete, sender=Teacher)
def add_post(instance, **kwargs):
	History.objects.create(
		post=instance.name,
		date=datetime.now()
	)




