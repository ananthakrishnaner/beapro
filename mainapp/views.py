from django.shortcuts import redirect, render
from .models import ContactForm
from django.core.mail import send_mail, BadHeaderError
from datetime import datetime
from django.utils.formats import localize

# Create your views here.

def index(request):
    if request.method == 'POST':
        name= request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']
        user_id = request.POST['user_id']
        date = localize(datetime.now())
        emailmsg = f'Hi Team,\nYou Reacived A Contact Submission {date} From User {user_id}\nUser Email: {email}\n\nMessage:\n{message}\n\n\t\n\tBEAPRO Email Support'
        user_contact = ContactForm.objects.create(name=name,phone=phone,subject=subject,email=email,message=message,user_id=user_id)
        user_contact.save()
        try:
            send_mail(subject, emailmsg, email, ['beapro1377@gmail.com'])
        except BadHeaderError:
            return redirect('/')
    else:
        pass
    
    return render(request,'main/index.html')