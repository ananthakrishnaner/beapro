from django.db.models.signals import post_save
from django.dispatch import receiver
from student.models import StudentProfile
from tutor.models import TutorProfile
from accounts.models import Account


@receiver(post_save,sender=Account)
def create_profile(sender,instance,created,**kwargs):
    if created:
        profile =  Account.object.get(username=instance)
        if profile.is_student:
            StudentProfile.objects.create(user=instance,fullname="UnknownStudent")
        else:
            if profile.is_tutor:
                TutorProfile.objects.create(user=instance,fullname="UnknownTutor")
            else:
                pass
