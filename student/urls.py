from django.urls import path,include
from .views import account_signup,account_login,logout_student


urlpatterns = [
    path('account/',account_login,name="student_account_login"),
    path('account/signup',account_signup,name="student_account_signup"),
    path('logout',logout_student, name="logout_student"),
]