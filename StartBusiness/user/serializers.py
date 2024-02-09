from rest_framework import serializers
from user.models import User
from django.contrib.auth.hashers import make_password



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_email', 'user_mobile_number','user_password','user_role','is_verify']
class UserLoginSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='user_mobile_number')
    class Meta:
       
        model = User
        fields = ('id','user_password')

class UserOtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('otp_key')
