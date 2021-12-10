from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,"login.html")

def my_account(request):
    return render(request, "my-account.html")