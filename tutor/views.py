from tutor.models import TutorProfile
from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth import logout
from accounts.models import Account
from .forms import UserProfileForm,TutorUpdateForm
from django.http import HttpResponse
import json
from student.models import ConnectionRequest

#create Tutor account
def account_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if Account.objects.filter(username=username).exists():
            messages.warning(request, 'Username already exist')
            return redirect('tutor_account_login')
        else:
            if Account.objects.filter(email=email).exists():
                messages.warning(request, 'Email already exist')
                return redirect('tutor_account_login')
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
    try:
        user = request.user
        tutor = TutorProfile.objects.get(user=user)
        account_verified = TutorProfile.objects.filter(user=user,verified=True).exists()
        if request.method == 'POST':
            u_form = UserProfileForm(request.POST,
                                    request.FILES,
                                    instance=request.user)
            t_form = TutorUpdateForm(request.POST,request.FILES,instance=tutor)
            if u_form.is_valid() and t_form.is_valid():
                u_form.save()
                t_form.save()
                return redirect('/')
        else:
            u_form = UserProfileForm(instance=request.user)
            t_form = TutorUpdateForm(instance=tutor)        

        context = {
            'u_form':u_form,
            't_form':t_form,
            'tutor':tutor,
            'account_verified':account_verified,
        }
        return render(request,'tutor/tutoreditprofile.html',context)

    except TutorProfile.DoesNotExist:
        print('no user')
        return redirect('tutor_account_login')


def connection_requests(request, *args, **kwargs):
    context = {}
    user=request.user
    if user.is_authenticated:
        user_id = kwargs.get("user_id")
        account = Account.objects.get(pk=user_id)
        
        if account == user:
            connection_requests = ConnectionRequest.objects.filter(receiver=account, is_active=True)
            context['connection_requests'] = connection_requests
        else:
            return HttpResponse("You can't view another users connection requests.")
    else:
        redirect("login")
    return render(request, "tutor/connection_request_list.html", context)


def decline_connection_request(request, *args, **kwargs):
    user = request.user
    payload = {}
    if request.method == "GET" and user.is_authenticated:
        connection_request_id = kwargs.get("connection_request_id")
        if connection_request_id:
            connection_request = ConnectionRequest.objects.get(pk=connection_request_id)
            # confirm that is the correct request
            if connection_request.receiver == user:
                if connection_request: 
                    # found the request. Now decline it
                    updated_notification = connection_request.decline()
                    payload['response'] = "connection request declined."
                else:
                    payload['response'] = "Something went wrong."
            else:
                payload['response'] = "That is not your connection request to decline."
        else:
            payload['response'] = "Unable to decline that connection request."
    else:
        # should never happen
        payload['response'] = "You must be authenticated to decline a connection request."
    return HttpResponse(json.dumps(payload), content_type="application/json")
