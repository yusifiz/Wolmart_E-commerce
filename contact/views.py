
from django.shortcuts import redirect, render
from . forms import ContactForm
from . models import Contact
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
def contact(request):
    
    messageSent = False
    
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = 'test'
            message = cd['message']
            send_mail(subject, message,settings.DEFAULT_FROM_EMAIL, ['memmedovh5@gmail.com',])
            messageSent = True
            form.save()
            return redirect('/')
        
    context = {
        'form':form,
        'messageSent': messageSent,
    }
    
    return render(request, 'contact-us.html', context)