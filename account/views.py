from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . forms import RegistrationForm , LoginForm
from django.contrib import messages
from account.tasks import send_confirmation_mail
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import authenticate, get_user_model, login as django_login, logout as django_logout
from account.tools.tokens import account_activation_token
from django.contrib.auth.decorators import login_required


# Create your views here.

User = get_user_model()

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
            send_confirmation_mail(user_id=user.id, site_address=site_address)
            messages.success(request, 'Siz ugurla qeydiyyatdan kecdiniz')
            return redirect(reverse_lazy('account:login'))
    context = {
        'form' : form
    }
    return render(request, 'register.html', context)

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Email is activated')
        return redirect(reverse_lazy('home:index'))
    elif user:
        messages.error(request, 'Email is not activated.')
        return redirect(reverse_lazy('account:register'))
    else:
        messages.error(request, 'Email is not activated')
        return redirect(reverse_lazy('account:register'))

def login(request):
    form = LoginForm()
    if request.method =='POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)
            if user:
                django_login(request, user)
                messages.success(request, 'Siz ugurla login oldunuz')
                return redirect(reverse_lazy('home:index'))
            else:
                messages.success(request, 'Siz login ola bilmediniz')
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)


def my_account(request):
    return render(request, "my-account.html")


@login_required
def logout(request):
    django_logout(request)
    return redirect(reverse_lazy('account:login'))