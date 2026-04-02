from rest_framework import serializers
from django.utils import timezone

from core import settings
from .models import *
from .utils import generate_otp_code, send_email


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.filter(email=validated_data.get("email"), is_active=False)
        if user.exists():
            sms = VerificationOTP.objects.get(user=user, type=VerificationOTP.VerificationType.REGISTER,
                                             expires_in__lt=timezone.now(), is_active=True)
            if sms:
                sms.expires_in = timezone.now() + settings.OTP_CODE_ACTIVATION_TIME
                code = generate_otp_code()
                sms.code = code
                send_email(code=code, email=user.email)

        user = User.objects.create(first_name=validated_data.get("first_name"),
                                   last_name=validated_data.get("last_name"),
                                   email=validated_data.get("email"),
                                   )
        user.set_password(validated_data.get("password"))
        user.save()
        return user


class VerifyOtpSerializer(serializers.Serializer):
    code = serializers.IntegerField(required=True)
    email = serializers.CharField(required=True)
    verify_type = serializers.ChoiceField(choices=VerificationOTP.VerificationType)


class ResetPasswordStartSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


class ResetPasswordFinishSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    verification = serializers.IntegerField(required=True)
    password = serializers.CharField(required=True)
    password_confirm = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password_confirm'):
            raise serializers.ValidationError('Passwords do not match')

        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')


class CreateUserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ('name', 'phone_number', 'apartment', 'street', 'pincode')


class UserAddressListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ('id', 'name', 'phone_number', 'apartment', 'street', 'pincode')