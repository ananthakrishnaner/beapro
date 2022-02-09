from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import TutorProfile
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

class TutorUpdateForm(forms.ModelForm):
    class Meta:
        model = TutorProfile
        fields = ('fullname','mobile','address','birth_date','collegeName','country','state','about_me',
        'experience','subject','individual','group','class_will_be_held_on','your_cv','qualification',
        'qualification_cert','social_profile','promo_video','amount','skills','subject_name'
        )

        widgets = {
            'fullname':forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Enter Full Name'}),
            'mobile':forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Enter mobile number ..'}),
            'address':forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Enter address'}),
            'birth_date':forms.DateInput(attrs={'class': 'form-control','placeholder' : 'dd/mm/yyyy','type':'date' }),
            'collegeName':forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Name',}),
            'subject_name':forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Tutoring Subject Name...',}),
            'country':forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Enter Your Country',}),
            'state':forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Enter Your State',}),
            'about_me': forms.Textarea(attrs={'class': 'form-control','placeholder' : 'Tell Us About Yourself',}),
            'skills': forms.Textarea(attrs={'class': 'form-control','placeholder' : 'Tell Us About Your Skills',}),
            'experience':forms.Textarea(attrs={'class': 'form-control','placeholder' : 'Tell Us About Your Expirence',}),
            'subject':forms.Select(attrs={'id':'format'}),
            'individual':forms.CheckboxInput(attrs={'class':'form-check-input','id':'flexCheckDefault'}),
            'group':forms.CheckboxInput(attrs={'class':'form-check-input','id':'flexCheckDefault'}),
            'class_will_be_held_on':forms.RadioSelect(attrs={'class':'form-check-input','id':'inlineRadio1'}),
            'your_cv':forms.FileInput(attrs={}),
            'qualification':forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Enter Highest Qualification'}),
            'qualification_cert':forms.FileInput(attrs={}),
            'social_profile':forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Your Social ID ,fb,youtube,linkedin ..'}),
            'promo_video':forms.FileInput(attrs={}),
            'amount':forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Amount Per Hour'}),
        }