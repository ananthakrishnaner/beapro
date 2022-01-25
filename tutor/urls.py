from django.urls import path
from .views import account_signup,account_login,logout_tutor,tutor_profile,connection_requests,decline_connection_request


urlpatterns = [
    path('account/',account_login,name="tutor_account_login"),
    path('account/signup',account_signup,name="tutor_account_signup"),
    path('logout',logout_tutor, name="logout_tutor"),

    path('profile/',tutor_profile, name="tutor_profile"),
    path('connection_requests/<user_id>/',connection_requests,name='connection-requests'),
    path('decline_connection_request/<connection_request_id>/', decline_connection_request, name='decline-connection-request'),

]
