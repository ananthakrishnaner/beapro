from django.urls import path,include
from .views import  index,tutorprofiles,viewprofile
from django.views.generic import TemplateView
from django.conf.urls import url

urlpatterns = [
    path('',index, name="index"),
    url(r'^service-worker.js', (TemplateView.as_view(template_name="app/service-worker.js", content_type='application/javascript', )), name='service-worker.js'),
    path('tutorprofiles',tutorprofiles, name="tutorprofiles"),
    path('tutorprofiles/<int:id>',viewprofile, name="viewprofile"),

]