from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import UserForm,ProfileForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request,'home.html')



def register(request):
    if request.method=='POST':
        userform=UserForm(request.POST)
        profileform=ProfileForm(request.POST)
        if userform.is_valid() and profileform.is_valid():
            user=userform.save()
            user.set_password(user.password)
            user.save()
            profile=profileform.save()
            profile.user=user
        else:
            print(userform.errors)
    else:
        userform=UserForm()
        profileform=ProfileForm()

    return render(request,'register.html',{
        'userform':userform,
        'profileform':profileform
    })



def loginuser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('invalid user')

    else:
        return render(request,'login.html')



@login_required
def logoutuser(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))