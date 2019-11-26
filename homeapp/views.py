from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from authapp import Forms
from authapp import models
from authapp.Forms import LoginForm
from authapp.models import registers


def home(request):
    return render(request,'index.html')


# def home(request):
#     loginform=LoginForm(request.POST)
#     if loginform.is_valid():
#         un=loginform.cleaned_data['email']
#         pw=loginform.cleaned_data['Password']
#         user=registers.objects.filter(email=un,Password=pw)
#         if not user:
#             return HttpResponse('index.html')
#         else:
#             login(request,user)
#             return render(request,'welcome.html')
#     else:
#         return render(request,'index.html')
#
# @login_required
# def login(request):
#     return render(request, "welcome.html")
# def my_logout(request):
#     logout(request)
#     return render(request,'index.html')
