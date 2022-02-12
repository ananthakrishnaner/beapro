import numbers
from webbrowser import get
from django.db import connections
from django.dispatch import receiver
from django.shortcuts import redirect, render

from accounts.models import Account
from .models import ContactForm
from django.core.mail import send_mail, BadHeaderError
from datetime import datetime
from django.utils.formats import localize
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import json
from django.contrib.auth.decorators import login_required
from datetime import datetime,timedelta,date

from .utils import *

from student.models import StudentProfile,ConnectionRequest,Coincheck
from tutor.models import TutorProfile
from student.utils import get_connection_request_or_false
from student.connection_request_status import ConnectionRequestStatus
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
        return redirect('/')
    else:
        try:
            if request.user.is_student:
                user = request.user
                student = StudentProfile.objects.get(user=user)
                featuredtutor = TutorProfile.objects.filter(featured=True)
                data = {
                    'student':student,
                    'featuredtutor':featuredtutor,
                    
                    }
                return render(request,'main/index.html',data)
            else:
                return render(request,'main/index.html')
        except:
            return render(request,'main/index.html')


@login_required(login_url='student_account_login')
def tutorprofiles(request):
    if request.user.is_student:
        tutorprofile = TutorProfile.objects.all()
        user = request.user
        student = StudentProfile.objects.get(user=user)
        if 'category' in request.GET:
            category = request.GET['category']
            if category != 'All':
                tutorprofile = TutorProfile.objects.filter(subject__iexact=category)
            else:
                tutorprofile = TutorProfile.objects.all()
            
            data ={
                'student':student,
                'tutorprofile':tutorprofile,
             }
            return render(request,'main/profilecard.html',data)
        else:
            tutorprofile = TutorProfile.objects.all()     
            data ={
                'student':student,
                'tutorprofile':tutorprofile,
            }
            return render(request,'main/profilecard.html',data)
    else:
        return redirect('index')



@login_required(login_url='student_account_login') 
def viewprofile(request,id):
    tutorprofile =  TutorProfile.objects.get(user_id = id) 
    is_self = True
    is_connection = False
    student = None
    connection_request = None
    request_sent = -1
    viewingprofile = TutorProfile.objects.filter(user=tutorprofile.user)
    connections = viewingprofile[0].connections.all()
    user = request.user
    if user.is_authenticated:
        username = request.user.username
        today = date.today()
        student = StudentProfile.objects.get(user=user)
        if Coincheck.objects.filter(name=username,coindate=today).exists():
            is_self = False
            if connections.filter(pk=user.id):
                is_connection = False
            else:
                is_connection = False
                #CASE1: requset sent
                if get_connection_request_or_false(sender=user,receiver=tutorprofile.user) != False:
                    request_sent = ConnectionRequestStatus.YOU_SENT_TO_THEM.value
                #Case2: no request
                else:
                    request_sent = ConnectionRequestStatus.NO_REQUEST_SENT.value

        elif student.wallet_amount > 9:
            Coincheck.objects.create(name=username,coindate=today)
            student.wallet_amount -=10
            student.prime_user =True
            student.save()
            return redirect(request.path)
        else:
            student.prime_user =False
            student.save()
            return redirect('/student/wallet/')

    elif not user.is_authenticated:
        is_self=False
    else:
        try:
            connection_request = ConnectionRequest.objects.filter(receiver=tutorprofile.user,is_active=True)
        except:
            pass
        
    data ={
        'student':student,
        'tutorprofile':tutorprofile,
        'is_connection':is_connection,
        'is_self':is_self,
        'request_sent':request_sent,
        'connection_request':connection_request
       
    }
    return render(request,'main/viewprofile.html',data)


def send_connection_request(request, *args, **kwargs):
	user = request.user
	payload = {}
	if user.is_authenticated:
		user_id = request.POST['receiver_user_id']
		if user_id:
			receiver = Account.objects.get(pk=user_id)
			#print(receiver)
            
			try:
				# Get any connection_requests requess (active and not-active)
				connection_requests = ConnectionRequest.objects.filter(sender=user, receiver=receiver)
				# find if any of them are active (pending)
				try:
					for request in connection_requests:
						if request.is_active:
							raise Exception("You already sent them a Connection request.")
					# If none are active create a new Connection request
					connection_requests = ConnectionRequest(sender=user, receiver=receiver)
					connection_requests.save()
					cr = ConnectionRequest.objects.filter(sender=user, receiver=receiver,is_active=True)
					payload['response'] = "Connection request sent."
					text = f'You Have a connection request from {user.studentprofile.fullname} from {user.studentprofile.state} '
					num=cr[0].receiver.tutorprofile.mobile
					send_sms(text,num)
				except Exception as e:
					payload['response'] = str(e)
			except ConnectionRequest.DoesNotExist:
				# There are no Connection requests so create one.
				connection_requests = ConnectionRequest(sender=user, receiver=receiver)
				connection_requests.save()
				payload['response'] = "Connection request sent."

			if payload['response'] == None:
				payload['response'] = "Something went wrong."
		else:
			payload['response'] = "Unable to sent a Connection request."
	else:
		payload['response'] = "You must be authenticated to send a Connection request."
	return HttpResponse(json.dumps(payload), content_type="application/json")
      

def accept_connection_request(request, *args, **kwargs):
    user = request.user
    payload = {}
    if request.method == "GET" and user.is_authenticated:
        connection_request_id = kwargs.get("connection_request_id")
        if connection_request_id:
            connection_request = ConnectionRequest.objects.get(pk=connection_request_id)
            print(connection_request.receiver)
            # confirm that is the correct request
            if connection_request.receiver == user:
                if connection_request: 
                    # found the request. Now accept it
                    updated_notification = connection_request.accept()
                    payload['response'] = "connection request accepted."
                    text = f'Your connection request as been accepted by {user.tutorprofile.fullname} all the best for your {user.tutorprofile.subject_name} learning'
                    num=connection_request.sender.studentprofile.mobile
                    send_sms(text,num)
                else:
                    payload['response'] = "Something went wrong."
            else:
                payload['response'] = "That is not your request to accept."
        else:
            payload['response'] = "Unable to accept that connection request."
    else:
        # should never happen
        payload['response'] = "You must be authenticated to accept a connection request."
    return HttpResponse(json.dumps(payload), content_type="application/json")
    


def remove_connection(request, *args, **kwargs):
    user = request.user
    payload = {}
    if request.method == "POST" and user.is_authenticated:
        user_id = request.POST.get("receiver_user_id")
        if user_id:
            try:
                removee = Account.objects.get(pk=user_id)
                print(removee)
                connection_list = StudentProfile.objects.get(user=user)
                connection_list.connectionterminate(removee)
                payload['response'] = "Successfully removed that connection."
            except Exception as e:
                payload['response'] = f"Something went wrong: {str(e)}"
        else:
            payload['response'] = "There was an error. Unable to remove that connection."
    else:
        # should never happen
        payload['response'] = "You must be authenticated to remove a connection."
    return HttpResponse(json.dumps(payload), content_type="application/json")



def cancel_connection_request(request, *args, **kwargs):
    user = request.user
    payload = {}
    if request.method == "POST" and user.is_authenticated:
        user_id = request.POST.get("receiver_user_id")
        if user_id:
            receiver = Account.objects.get(pk=user_id)
            try:
                connection_requests =   ConnectionRequest.objects.filter(sender=user, receiver=receiver, is_active=True)
            except  ConnectionRequest.DoesNotExist:
                payload['response'] = "Nothing to cancel. connection request does not exist."

            # There should only ever be ONE active connection request at any given time. Cancel them all just in case.
            if len(connection_requests) > 1:
                for request in connection_requests:
                    request.cancel()
                payload['response'] = "connection request canceled."
            else:
                # found the request. Now cancel it
                connection_requests.first().cancel()
                payload['response'] = "connection request canceled."
        else:
            payload['response'] = "Unable to cancel that connection request."
    else:
        # should never happen
        payload['response'] = "You must be authenticated to cancel a connection request."
    return HttpResponse(json.dumps(payload), content_type="application/json")