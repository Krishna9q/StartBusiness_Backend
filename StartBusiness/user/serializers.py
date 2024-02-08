from rest_framework import serializers
from user.models import User
from django.contrib.auth.hashers import make_password


userlogin = ['user_email', 'user_mobile_number']
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
class UserLoginSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='user_mobile_number')
    class Meta:
       
        model = User
        fields = ('id','user_password')


