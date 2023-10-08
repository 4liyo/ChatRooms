from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def signUp(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            fname = form.cleaned_data['username']
            # login(request, user)
            messages.success(request, f'Successfully added {fname}')
            return redirect('login')

    form = SignUpForm(request.POST)
    return render(request, "core/signup.html", {'form':form})

def logIn(request):    
    return render(request, "core/login.html")
