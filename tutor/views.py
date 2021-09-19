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
        if Account.objects.filter(username=username).exists():
            messages.warning(request, 'Username already exist')
            return redirect('/')
        else:
            if Account.objects.filter(email=email).exists():
                messages.warning(request, 'Email already exist')
                return redirect('/')
            else:
                
                user = Account.objects.create_user(username=username,email=email ,password=password,tutor=True,student=False)
                user.save()

                messages.success(request, 'Account created successfully')
                return render(request,'tutor/logint.html')
    return render(request,'tutor/logint.html')

#Tutor Login

def account_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if len(password) > 50:
            messages.warning(request, 'Detected malicious Attempt :(')
            return redirect('tutor_account_login')
        else:
            user1 = auth.authenticate(email=email,password=password)
            if user1 is not None:
                if user1.is_tutor == True:
                    auth.login(request,user1)
                    return redirect('/')
                else:
                    pass
            else:
                messages.warning(request, 'Invalid Credentials')
                return redirect('tutor_account_login')
    return render(request,'tutor/logint.html')


# Tutor logout
def logout_tutor(request):
    logout(request)
    return redirect('tutor_account_login')


#Tutor Profile
def tutor_profile(request):
    return render(request,'tutor/tutoreditprofile.html')