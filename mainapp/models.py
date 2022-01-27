from datetime import date, datetime
from django.db import models
from datetime import datetime
from student.models import StudentProfile
from tutor.models import TutorProfile


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

# class RelationshipManager(models.Manager):
#     def invatations_received(self, receiver):
#         qs = Relationship.objects.filter(receiver=receiver, status='send')
#         return qs


# STATUS_CHOICES = (
#     ('send', 'send'),
#     ('accepted', 'accepted')
# )

# class Relationship(models.Model):
#     sender = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='sender')
#     receiver = models.ForeignKey(TutorProfile, on_delete=models.CASCADE, related_name='receiver')
#     status = models.CharField(max_length=8, choices=STATUS_CHOICES)
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)

#     objects = RelationshipManager()

#     def __str__(self):
#         return f"{self.sender}-{self.receiver}-{self.status}"