from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . forms import RegistrationForm
from django.contrib import messages

# Create your views here.

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(data =request.POST, files = request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password = form.cleaned_data.get('password1')
            user.is_active = False
            user.save()
            site_address = request.is_secure() and "https://" or "http://" + request.META['HTTP_HOST']  # https
            messages.success(request, 'Siz ugurla qeydiyyatdan kecdiniz')
            return redirect(reverse_lazy('account:login'))
    context = {
        'form' : form
    }
    return render(request, 'register.html', context)

def login(request):
    return render(request,"login.html")

def my_account(request):
    return render(request, "my-account.html")

