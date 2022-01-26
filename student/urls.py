from django.urls import path,include
from .views import account_signup,account_login,logout_student,student_profile,student_wallet,payment_status,mytutor,remove_connection_tutor,student_view_profile


urlpatterns = [
    path('account/',account_login,name="student_account_login"),
    path('account/signup',account_signup,name="student_account_signup"),
    path('logout',logout_student, name="logout_student"),

    path('profile/',student_profile, name="student_profile"),
    path('studentview/<int:id>',student_view_profile, name="student-view-profile"),
    path('mytutor/',mytutor, name="mytutor"),
    path('remove_connection_tutor/',remove_connection_tutor,name='remove-connection-tutor'),
    path('wallet/',student_wallet, name="student_wallet"),
    path('wallet/payment-status/', payment_status, name='payment-status')
]
