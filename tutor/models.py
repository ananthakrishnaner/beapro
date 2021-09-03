from django.db import models
from accounts.models import Account
from datetime import datetime
# Create your models here.

class TutorProfile(models.Model):
    user = models.OneToOneField(Account,on_delete=models.CASCADE)
    fullname = models.CharField(max_length=30)

    def __str__(self):
        return self.fullname