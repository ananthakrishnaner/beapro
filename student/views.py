from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from accounts.models import Account
from django.contrib import messages,auth
from django.contrib.auth import logout
from .models import StudentProfile
from .forms import UserProfileForm,StudentUpdateForm



#create student account
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
                
                user = Account.object.create_user(username=username,email=email ,password=password)
                #Account.is_student = True
                #assign_role(user,'agent')
                messages.success(request, 'Account created successfully')
                return redirect('/')
    return render(request,'student/login.html')

#create login student account
def account_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if len(password) > 50:
            messages.warning(request, 'Detected malicious Attempt :(')
            return redirect('student/login.html')
        else:
            user1 = auth.authenticate(email=email,password=password)
            if user1 is not None:
                auth.login(request,user1)
                return redirect('/')
            else:
                messages.warning(request, 'Invalid Credentials')
                return redirect('login')

    return render(request,'student/login.html')


# student logout
def logout_student(request):
    logout(request)
    return redirect('student_account_login')


def student_profile(request):
    user = request.user.id
    
    try:
        student = StudentProfile.objects.get(id=user)
    except:
        student = StudentProfile.objects.create(user=request.user,fullname='unknown')
        student.save()
    
    if request.method == 'POST':
        u_form = UserProfileForm(request.POST,
                                request.FILES,
                                instance=request.user)
        s_form = StudentUpdateForm(request.POST,instance=student)
        ak =request.POST.get('profile_image')
        print(f'ak bro {ak}')
        if u_form.is_valid() and s_form.is_valid():
            u_form.save()
            s_form.save()
            return redirect('/')
    else:
        u_form = UserProfileForm(instance=request.user)
        s_form = StudentUpdateForm(instance=student)        

    context = {
        'u_form':u_form,
        's_form':s_form,
    }
    return render(request,'student/editprofile.html',context)