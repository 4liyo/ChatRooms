from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def signUp(request):
    return render(request, "core/signup.html")

def logIn(request):
    return render(request, "core/login.html")