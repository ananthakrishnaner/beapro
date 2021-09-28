from django.contrib.auth.models import AnonymousUser
from django.db import models
from django.db.models.expressions import F
from accounts.models import Account
from datetime import datetime

# Create your models here.

class StudentProfile(models.Model):
    user = models.OneToOneField(Account,on_delete=models.CASCADE)
    fullname = models.CharField(max_length=30)
    mobile = models.CharField(max_length=15)
    Interest = models.CharField(max_length=45,blank=True)
    birth_date = models.DateField(blank=True,null=True)
    collegeName = models.CharField(max_length=60,blank=True)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50,blank=True)
    wallet_amount = models.IntegerField(blank=True,null=True,default=10)
    is_allowed_to_publish = models.BooleanField(default=False)
    prime_user = models.BooleanField(default=False)
    account_verified = models.BooleanField(default=False)
    is_allowd_view_blog = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    prime_expire = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.fullname

class Coincheck(models.Model):
    name=models.CharField(max_length=30,blank=True)
    coindate = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.name

class StudentTransaction(models.Model):
    fullname = models.CharField(max_length=30,blank=True)
    email = models.EmailField(blank=True)
    amount = models.CharField(max_length=30,blank=True)
    order_id = models.CharField(max_length=130,blank=True)
    payment_id = models.CharField(max_length=130,blank=True)
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
 

    def __str__(self):
        return self.fullname

