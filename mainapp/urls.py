from django.urls import path,include
from .views import  index,tutorprofiles,viewprofile,faq,send_connection_request,accept_connection_request,remove_connection,cancel_connection_request
from django.views.generic import TemplateView
from django.conf.urls import url


urlpatterns = [
    path('',index, name="index"),
    path('faq/',faq, name="faq"),
    url(r'^service-worker.js', (TemplateView.as_view(template_name="app/service-worker.js", content_type='application/javascript', )), name='service-worker.js'),
    path('tutorprofiles',tutorprofiles, name="tutorprofiles"),
    path('tutorprofiles/<int:id>',viewprofile, name="viewprofile"),
    path('connection_request/', send_connection_request, name='connection-request'),
    path('accept_connection_request/<connection_request_id>/', accept_connection_request, name='accept-connection-request'),
    path('remove_connection/', remove_connection, name='remove-connection'),
     path('connection_request_cancel/', cancel_connection_request, name='connection-request-cancel'),

]