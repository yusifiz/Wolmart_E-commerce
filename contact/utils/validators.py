
from django.core.exceptions import ValidationError
def mail_validator(mail):
    if not mail.endswith("gmail.com"):
        raise ValidationError('Daxil edilen mail gmail.com ile bitmelidir')
    return True