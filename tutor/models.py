from django.db import models
from django.db.models.fields import IntegerField
from accounts.models import Account
from datetime import datetime
# Create your models here.



class TutorProfile(models.Model):

    subject_choices = (
        ('Mathematics' , 'Mathematics'),
        ('History' , 'History'),
        ('Programming' , 'Programming'),
        ('Music' , 'Music'),
        ('Chemistry' , 'Chemistry'),
        ('Physics' , 'Physics'),
        ('Languages' , 'Languages'),
        ('Other' , 'Other'),
    )

    Classes_will_be_held_on_choice = (
        ('Online','Online'),
        ('Your Home','Your Home'),
        ('At my home','At my home'),
    )

    user = models.OneToOneField(Account,on_delete=models.CASCADE)
    fullname = models.CharField(max_length=30)
    mobile = models.CharField(max_length=15)
    address = models.CharField(max_length=55)
    birth_date = models.DateField(blank=True,null=True)
    collegeName = models.CharField(max_length=60,blank=True)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50,blank=True)
    about_me = models.TextField(max_length=700)
    experience = models.TextField(max_length=700)
    subject = models.CharField( choices=subject_choices, max_length=20,null=True, default=None)
    individual = models.BooleanField(default=False)
    group = models.BooleanField(default=False)
    class_will_be_held_on = models.CharField( choices=Classes_will_be_held_on_choice, max_length=20,null=True, default=None)
    your_cv = models.FileField(upload_to='tutor/documents/cv/%Y-%m-%d',blank=True)
    qualification = models.CharField(max_length=35)
    qualification_cert = models.FileField(upload_to='tutor/documents/edu/%Y-%m-%d',blank=True)
    social_profile = models.URLField(max_length=300,blank=True)
    promo_video = models.FileField(upload_to='tutor/documents/promo_video/%Y-%m-%d',default='default_img/promo_video.mp4',blank=True)
    amount = models.IntegerField(default=100)
    response_time = models.CharField(max_length=20,default='48')
    connections = models.ManyToManyField(Account,blank=True,related_name='connections_t')
    created = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.fullname

    def __str__(self):
        return f"{self.user.username}-{self.created.strftime('%d-%m-%Y')}"

    def get_connections(self):
        return self.connections.all()

    def get_connections_no(self):
        return self.connections.all().count()