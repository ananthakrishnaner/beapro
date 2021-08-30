from datetime import date, datetime
from django.db import models
from datetime import datetime

# Create your models here.

class ContactForm(models.Model):
    name = models.CharField(max_length=55)
    email = models.EmailField()
    phone = models.CharField(max_length=20,blank=True)
    subject = models.CharField(max_length=35)
    message = models.TextField(max_length=200)
    user_id = models.CharField(max_length=10,blank=True)
    created_date = models.DateTimeField(default=datetime.now,null=True)
    

    def __str__(self):
        return self.name