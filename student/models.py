from django.contrib.auth.models import AnonymousUser
from django.db import connections, models
from django.db.models.expressions import F
from django.dispatch import receiver
from accounts.models import Account
from datetime import datetime
from tutor.models import TutorProfile

# Create your models here.

class StudentProfile(models.Model):
    user = models.OneToOneField(Account,on_delete=models.CASCADE)
    fullname = models.CharField(max_length=30)
    mobile = models.CharField(max_length=15)
    Interest = models.CharField(max_length=45,blank=True)
    about_me = models.TextField(max_length=700,blank=True)
    birth_date = models.DateField(blank=True,null=True)
    collegeName = models.CharField(max_length=60,blank=True)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50,blank=True)
    wallet_amount = models.IntegerField(blank=True,null=True,default=10)
    is_allowed_to_publish = models.BooleanField(default=False)
    connections = models.ManyToManyField(Account,blank=True,related_name='connections_s')
    prime_user = models.BooleanField(default=False)
    account_verified = models.BooleanField(default=False)
    is_allowd_view_blog = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    prime_expire = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.fullname
 
 #Add tutor
    def add_connection(self, account):
        if not account in self.connections.all():
            self.connections.add(account)
#Remove Tutor 
    def remove_connection(self,account):
        if account in self.connections.all():
            self.connections.remove(account)
        
    def connectionterminate(self,removee):
        remover_connection_list = self # person terminating the friendship
        remover_connection_list.remove_connection(removee)
        connection_list = TutorProfile.objects.get(user=removee)
        connection_list.remove_connection(remover_connection_list.user)

    def is_mutual_connection(self, connection):
        """
        Is this a friend?
        """
        if connection in self.connection.all():
            return True
        return False   


    def get_connections(self):
        return self.connections.all()


    def get_connections_no(self):
        return self.connections.all().count()

    def __str__(self):
        return f"{self.user.username}-{self.created.strftime('%d-%m-%Y')}"
    

class ConnectionRequest(models.Model):
    sender = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="sender")
    receiver = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="receiver")
    is_active = models.BooleanField(blank=True,null=False,default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender.username
    
    def accept(self):
        receiver_connection_list = TutorProfile.objects.get(user=self.receiver)
        if receiver_connection_list:
            receiver_connection_list.add_connection(self.sender)
            sender_connection_list = StudentProfile.objects.get(user=self.sender)
            if sender_connection_list:
                sender_connection_list.add_connection(self.receiver)
                self.is_active=False
                self.save()

    def decline(self):
        self.is_active = False
        self.save()

    def cancel(self):
        self.is_active = False
        self.save()



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

