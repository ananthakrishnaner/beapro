from django.urls import path,include
from .views import  index,tutorprofiles,viewprofile

urlpatterns = [
    path('',index, name="index"),
    path('tutorprofiles',tutorprofiles, name="tutorprofiles"),
    path('tutorprofiles/<int:id>',viewprofile, name="viewprofile"),

]