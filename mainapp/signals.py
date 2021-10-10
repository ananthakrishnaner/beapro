from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from student.models import StudentProfile
from tutor.models import TutorProfile
from .models import Relationship
from accounts.models import Account
from datetime import datetime


@receiver(post_save,sender=Account)
def create_profile(sender,instance,created,**kwargs):
    if created:
        date = datetime.now()
        profile =  Account.objects.get(username=instance)
        if profile.is_student:
            StudentProfile.objects.create(user=instance,fullname="UnknownStudent",prime_expire=date)
        else:
            if profile.is_tutor:
                TutorProfile.objects.create(user=instance,fullname="UnknownTutor")
            else:
                pass

@receiver(post_save, sender=Relationship)
def post_save_add_to_connections(sender, instance, created, **kwargs):
    sender_ = instance.sender
    receiver_ = instance.receiver
    if instance.status == 'accepted':
        sender_.connections.add(receiver_.user)
        receiver_.connections.add(sender_.user)
        sender_.save()
        receiver_.save()