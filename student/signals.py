from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import StudentProfile
from accounts.models import Account


@receiver(post_save,sender=Account)
def create_profile(sender,instance,created,**kwargs):
    if created:
        StudentProfile.objects.create(user=instance,fullname="UnknownName")



# @receiver(post_save,sender=Account)
# def save_profile(sender,instance,**kwargs):
#     instance.StudentProfile.save()