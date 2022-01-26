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
        'class': 'form-control',
        'id': 'imageUpload',
    }))

    class Meta:
        model=Account
        fields=['email','profile_image']


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['fullname','mobile','Interest','about_me','birth_date','collegeName','country','state']

        widgets = {
            'fullname':forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Enter Full Name'}),
            'mobile':forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Enter mobile number ..'}),
            'Interest':forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Enter Interest'}),
            'about_me': forms.Textarea(attrs={'class': 'form-control','placeholder' : 'Tell Us About Yourself',}),
            'birth_date':forms.DateInput(attrs={'class': 'form-control','placeholder' : 'dd/mm/yyyy','type':'date' }),
            'collegeName':forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Name',}),
            'country':forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Enter Your Country',}),
            'state':forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Enter Your State',}),
        }
