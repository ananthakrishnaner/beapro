from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth import logout

from accounts.models import Account



#create Tutor account
def account_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if Account.object.filter(username=username).exists():
            messages.warning(request, 'Username already exist')
            return redirect('/')
        else:
            if Account.object.filter(email=email).exists():
                messages.warning(request, 'Email already exist')
                return redirect('/')
            else:
                
                user = Account.object.create_user(username=username,email=email ,password=password,tutor=True,student=False)
                user.save()

                messages.success(request, 'Account created successfully')
                return redirect('tutor_account_login')
    return render(request,'tutor/logint.html')

#Tutor Login
def account_login(request):
    return render(request,'tutor/logint.html')
