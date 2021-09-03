from django.urls import path
from .views import account_signup,account_login


urlpatterns = [
    path('account/',account_login,name="tutor_account_login"),
    path('account/signup',account_signup,name="tutor_account_signup"),

]
