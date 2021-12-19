from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage, message
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from account.tools.tokens import account_activation_token


User = get_user_model()

def send_confirmation_mail(user_id, site_address):
    user = User.objects.filter(id=user_id).first()
    from_email = settings.EMAIL_HOST_USER
    recipient = user.email
    subject = 'Please, confirm your account'
    context = {
        'user' : user,
        'site_address' : site_address,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),

    }
    body = render_to_string('emails/email_confirmation.html', context)
    mail = EmailMessage(subject, to=[recipient, ], from_email=from_email, body=body)
    mail.content_subtype = 'html'
    mail.send(fail_silently=True)