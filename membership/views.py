from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.
def LoginView(request):
  context = {}
  return render(request, 'membership/login.html', context)

def LogoutView(request):
  context = {}
  return render(request, 'membership/register.html', context)

def RegisterView(request):
  context = {}
  return render(request, 'membership/register.html', context)

def IndexView(request):
  context = {}
  return render(request, 'membership/index.html', context)

def ProfileView(request):
  context = {}
  return render(request, 'membership/profile.html', context)

def ChangePasswordView(request):
  context = {}
  return render(request, 'membership/change_password.html', context)

def ForgotPasswordView(request):
  context = {}
  return render(request, 'membership/forgot_password.html', context)