from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import StudentProfile
from accounts.models import Account



class UserProfileForm(forms.ModelForm):
    email = forms.EmailField(max_length=50,widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder' : 'Enter email id',
        'type' : 'email',
    }))
    profile_image = forms.ImageField(widget=forms.FileInput(attrs={
        'class':'pic',
    }))

    class Meta:
        model=Account
        fields=['email','profile_image']


class StudentUpdateForm(forms.ModelForm):
    fullname = forms.CharField(widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Enter Full Name',
                'maxlength' :30,
            }))
    mobile = forms.CharField(widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Enter Mobile Number',
                'maxlength' :10,
            }))
    Interest = forms.CharField(widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Interested in...',
                'maxlength' :30,
            }))
    birth_date = forms.DateField(widget=forms.DateInput(attrs={
                'class': 'form-control',
                'type' : 'date',
                'placeholder' : 'dd/mm/yyyy',
                
            }))
    collegeName = forms.CharField(widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Name',
                'maxlength' :30,
            }))
    country = forms.CharField(widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Country',
                'maxlength' :30,
            }))
    state = forms.CharField(widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'State',
                'maxlength' :30,
            }))
    class Meta:
        model = StudentProfile
        fields = ['fullname','mobile','Interest','birth_date','collegeName','country','state']



