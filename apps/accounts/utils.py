import random

from django.core.mail import send_mail
from rest_framework.exceptions import ValidationError

from core import settings


def check_otp_code(value):
    if len(value) != 6:
        raise ValidationError('Must be exactly 6 digits')


def send_email(code, email):
    message = f'Your otp code is {code}'
    send_mail(
        subject='OTP Code',
        message=message,
        from_email=settings.EMAIL_HOST_USER,
    recipient_list=[email],
    fail_silently=False,)


def generate_otp_code():
    number = random.randint(100000, 999999)
    return str(number)


