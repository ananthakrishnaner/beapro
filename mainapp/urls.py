from django.urls import path,include
from .views import  index,tutorprofiles

urlpatterns = [
    path('',index, name="index"),
    path('t',tutorprofiles, name="tutorprofiles"),
]