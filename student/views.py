from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from accounts.models import Account
from django.contrib import messages,auth
from django.contrib.auth import logout
from .models import StudentProfile,StudentTransaction
from .forms import UserProfileForm,StudentUpdateForm
from .decorators import prime_user
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest

#create student account
def account_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if Account.objects.filter(username=username).exists():
            messages.warning(request, 'Username already exist')
            return redirect('student_account_login')
        else:
            if Account.objects.filter(email=email).exists():
                messages.warning(request, 'Email already exist')
                return redirect('student_account_login')
            else:
                
                user = Account.objects.create_user(username=username,email=email ,password=password,tutor=False,student=True)
                user.save()
                messages.success(request, 'Account created successfully')
                return redirect('student_account_login')
    return render(request,'student/login.html')

#create login student account
def account_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if len(password) > 50:
            messages.warning(request, 'Detected malicious Attempt :(')
            return redirect('student_account_login')
        else:
            user1 = auth.authenticate(email=email,password=password)
            if user1 is not None:
                auth.login(request,user1)
                return redirect('/')
            else:
                messages.warning(request, 'Invalid Credentials')
                return redirect('student_account_login')


    return render(request,'student/login.html')


# student logout
def logout_student(request):
    logout(request)
    return redirect('student_account_login')


# Edit Profile

def student_profile(request):
    
    try:
        user = request.user
        student = StudentProfile.objects.get(user=user)
        account_verified = StudentProfile.objects.filter(user=user,account_verified=True)
        if request.method == 'POST':
            u_form = UserProfileForm(request.POST,
                                    request.FILES,
                                    instance=request.user)
            s_form = StudentUpdateForm(request.POST,instance=student)
            if u_form.is_valid() and s_form.is_valid():
                u_form.save()
                s_form.save()
                messages.success(request, 'Account Updated')
                return redirect('student_profile')
            else:
                messages.warning(request, 'Somethng went wrong :(')
                return redirect('student_profile')
        else:
            u_form = UserProfileForm(instance=request.user)
            s_form = StudentUpdateForm(instance=student)        

        context = {
            'u_form':u_form,
            's_form':s_form,
            'student':student,
            'account_verified':account_verified,
        }
        return render(request,'student/editprofile.html',context)

    except StudentProfile.DoesNotExist:
        print('no user')
        return redirect('student_account_login')


# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))


#Student wallet
def student_wallet(request):
    user = request.user
    student = StudentProfile.objects.get(user=user)
    currency = 'INR'
    useremail = request.user.email
    if request.method == 'POST':
        name = student.fullname
        org_amount = request.POST['amount']
        amount = int(org_amount) * 100
        response_payment  = razorpay_client.order.create(dict(amount=amount,currency=currency))
        order_id = response_payment['id']
        order_status = response_payment['status']
        if order_status == 'created':
            beapro_payment = StudentTransaction(
                fullname=name,
                email = useremail,
                amount=org_amount,
                order_id=order_id
            )
            beapro_payment.save()
            response_payment['name'] = name

        
        context = {
            'payment': response_payment,
            'amount':amount,
            'name':name,
            'razorpay_merchant_key':settings.RAZOR_KEY_ID,
        }
        return render(request,'student/swallet.html',context=context)
    else:
        transaction = StudentTransaction.objects.filter(email=useremail).order_by('-created')
        data = {
            'student':student,
            'currency':currency,
            'transaction':transaction,
        }
        return render(request,'student/swallet.html',data)


# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def payment_status(request):
    response = request.POST
    user = request.user
    print(response)
    params_dict = {
        'razorpay_order_id': response['razorpay_order_id'],
        'razorpay_payment_id': response['razorpay_payment_id'],
        'razorpay_signature': response['razorpay_signature']
    }

    # client instance
    client = razorpay_client
    order_id = response['razorpay_order_id']
    try:
        status = client.utility.verify_payment_signature(params_dict)
        transaction = StudentTransaction.objects.get(order_id=response['razorpay_order_id'])
        transaction.paid =True
        transaction.payment_id = response['razorpay_payment_id']
        transaction.save()
        ords = client.order.fetch(order_id)
        paid_amt = ords['amount_paid']
        if paid_amt == 2000:
            stdprofile = StudentProfile.objects.get(user=user)
            stdprofile.wallet_amount +=stdprofile.wallet_amount + 100
            stdprofile.save()
        elif paid_amt == 5500:
            stdprofile = StudentProfile.objects.get(user=user)
            stdprofile.wallet_amount +=stdprofile.wallet_amount + 300
            stdprofile.save()

        elif paid_amt == 16000:
            stdprofile = StudentProfile.objects.get(user=user)
            stdprofile.wallet_amount +=stdprofile.wallet_amount + 900
            stdprofile.save()
        elif paid_amt == 32000:
            stdprofile = StudentProfile.objects.get(user=user)
            stdprofile.wallet_amount +=stdprofile.wallet_amount + 1800
            stdprofile.save()
        else:
            stdprofile = StudentProfile.objects.get(user=user)
            stdprofile.wallet_amount +=stdprofile.wallet_amount - 10
            stdprofile.save()
        return render(request,'student/payment-success.html',{'status': True,'paid_amt':paid_amt})
    except:
        return render(request,'student/payment-success.html',{'status': False})

