from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect,HttpResponse
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,'base.html',context={})


def signUp(request):
    registered = False
    if request.method=="POST":
        signup = SignUpForm(data = request.POST)
        if signup.is_valid():
            signup.save()
            registered = True
    else:
        signup = SignUpForm()

    dict = {'form':signup,'registered':registered}
    return render(request,'login_app/register.html',context=dict)

def signIn(request):
    success = False
    if request.method == "POST":
        signin = AuthenticationForm(data = request.POST)
        if signin.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user:
                login(request, user)
                success = True
            else:
                return HttpResponse("Not active")
        else:
            return HttpResponse("Invalid")

    else:
        signin = AuthenticationForm()

    dict = {'form':signin,'success':success}
    return render(request, 'login_app/login.html',context=dict)

@login_required
def signOut(request):
    logout(request)
    return render(request,'base.html',context = {})
