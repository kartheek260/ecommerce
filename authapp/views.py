import http
import http.client

from django import forms
from django.conf import settings
import json
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
import random
from authapp.Forms import RegForm
from .models import registers
from authapp.Forms import LoginForm


def signup(request):
    if request.method == 'POST':
        regform = RegForm(request.POST)
        if regform.is_valid():
            x = otp_send(request)
            if x:
                return render(request, 'includes/otp_input.html')
            else:
                return render(request, 'signup.html')
        else:
            return render(request, 'signup.html')
    else:
        return render(request, 'signup.html')


def otpvalidation(request):
    newotp = request.POST['otp']
    oldotp = request.session['otp']
    if newotp == oldotp:
        form = RegForm(request.session["details"])
        new_user = User.objects.create_user(username=request.session["un"], password=request.session["pw"])
        new_user.save()
        form.save()
        login(request,new_user)  #login is a function
        return render(request,'welcome.html')
    else:
        return render(request, 'includes/otp_input.html')


def otp_send(request):
    ot = str(random.randint(100000, 999999))
    # request.session["pwd"]=request.POST["t1"]
    phone = request.POST["phone"]
    # temail=request.POST["email"]
    request.session["un"]=request.POST["email"]
    request.session["pw"] = request.POST["Password"]
    subject = "registration otp"
    # From_mail=settings.EMAIL_HOST_USER
    # to_list=[temail]
    # send_mail(subject, ot, From_mail, to_list, fail_silently=False)
    print("otp sent to email")
    request.session["details"]=request.POST
    request.session["otp"] = ot
    conn = http.client.HTTPSConnection("api.msg91.com")

    payload = "{ \"sender\": \"KARTHK\", \"route\": \"4\", \"country\": \"91\", \"sms\": [ { \"message\": \"" + ot + "\", \"to\": [ \"" + phone +"\" ]}]}"

    headers = {
        'authkey': "295863A5LW905fm05d8b401e",
        'content-type': "application/json"
    }

    conn.request("POST", "/api/v2/sendsms?country=91", payload, headers)

    #res = conn.getresponse()
    #data = res.read()

    #k=data.decode("utf-8")
    data = conn.getresponse()
    res = json.loads(data.read().decode("UTF-8"))
    print(res)

    if res["type"] == "success":
        return True
    else:
        return False


# Create your views here.
def signin(request):
    if request.method=="POST":
        loginform=LoginForm(request.POST)
        if loginform.is_valid():
            un=loginform.cleaned_data['email']
            pw=loginform.cleaned_data['Password']
            dbuser=registers.objects.filter(email=un,Password=pw)
            if not dbuser:
                return HttpResponse('Login Failed')
            else:
                login(request,dbuser)
                return render(request,'welcome.html')
    else:
        return render(request, 'registration/login.html')


@login_required
def login(request):
    return render(request, "welcome.html")

def my_logout(request):
    logout(request)
    return render(request,'index.html')

