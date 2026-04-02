from django.db.models.signals import post_save
from django.dispatch import receiver

from core.settings import OTP_CODE_ACTIVATION_TIME
from .models import User, VerificationOTP
from .utils import generate_otp_code, send_email
from datetime import datetime, timedelta

@receiver(post_save, sender=User)
def create_verification_otp(sender, instance, created, **kwargs):
    if created:
        code = generate_otp_code()
        VerificationOTP.objects.create(user=instance, type=VerificationOTP.VerificationType.REGISTER,
                                      code=code,
                                      expires_in=datetime.now() + timedelta(minutes=OTP_CODE_ACTIVATION_TIME))
        send_email(code=code, email=instance.email)
        print("Signal is working")