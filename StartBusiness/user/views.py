from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from user.serializers import UserLoginSerializer, UserSerializer,UserOtpSerializer
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password , check_password
from user.models import User
from rest_framework_simplejwt.tokens import RefreshToken
import random
from datetime import datetime
import json
from StartBusiness.email import send_verification_email

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'access': str(refresh.access_token),
        'refresh': str(refresh)
    }
def otp_generator(id,data):
   user = User.objects.get(user_email=id)
   user.otp_key = data
   user.save()

class UserRegisterView(GenericAPIView):
    serializer_class = UserSerializer
    def post(self, request , format=None):
      if User.objects.filter(user_email=request.data.get('user_email')).count() >=1 or User.objects.filter(user_mobile_number=request.data.get('user_mobile_number')).count() >=1:
          Response.status_code = status.HTTP_400_BAD_REQUEST
          return Response({
            'status' : status.HTTP_400_BAD_REQUEST,
            'message' : "this user is already registerd"
                      })
      else:
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.validated_data['user_password']=make_password(serializer.validated_data['user_password'])
        serializer.save()
        Response.status_code = status.HTTP_201_CREATED
        otp = [random.randint(1, 100) for _ in range(4)]
        d = json.dumps([{'otp': otp, 'timestamp': datetime.now().strftime('%H:%M:%S')}])
        id = request.data.get('user_email')
        otp_generator(id, d)
        send_verification_email(otp, id)
        # print(random_numbers)
        return Response({
                 'status': status.HTTP_200_OK,
                 'message': " User Successfully registered"
                                   })
        
class UserOtpVerificationEmail(GenericAPIView):
    def post(self, input, request, format=None):
        pass


class UserView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, input=None, format=None):
        id = input
        if id is not None:
            if User.objects.filter(user_id=id).count() >= 1:
                user  = User.objects.get(user_id=id)
                serializer = UserSerializer(user)
                Response.status_code = status.HTTP_200_OK
              
                return Response(
                    {
                        'status': status.HTTP_200_OK,
                        'message': "user " + 'data retrieved successfully',
                        'data': serializer.data,
                    }
                )
            else:
                Response.status_code = status.HTTP_400_BAD_REQUEST
                return Response(
                    {
                        'status': status.HTTP_400_BAD_REQUEST,
                        'message': "Invalid user id",
                    },
                )
        else:
            user = User.objects.all()    
            serializer = UserSerializer(user, many=True)
            Response.status_code = status.HTTP_200_OK
            return Response({
                 'status': status.HTTP_200_OK,
                 'message': "user " + 'data retrieved successfully',
                 'data': serializer.data,
            })
        
class UserUpdateView(APIView):
    # permission_classes = [IsAuthenticated]

    def patch(self, request, input, format=None):
        id = input
        if User.objects.filter(user_id=id).count() >= 1:
            user = User.objects.get(user_id=id)
            serializer = UserSerializer(user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            if request.data.get('user_password') is not None:
             serializer.validated_data['user_password']=make_password(serializer.validated_data['user_password'])
            serializer.save()
            Response.status_code = status.HTTP_200_OK
            return Response(
                {
                    'status': status.HTTP_200_OK,
                    'message': 'user Updated Successfully' 
                },
            )
        else:
            Response.status_code = status.HTTP_400_BAD_REQUEST
            return Response(
                {
                    'status': status.HTTP_400_BAD_REQUEST,
                    'message': 'invalid id',
                },
            )

class UserLoginView(GenericAPIView):
   serializer_class = UserLoginSerializer
   def post (self, request,format=None):
      id = request.data.get('id')
      password = request.data.get('user_password')
     
      if User.objects.filter(user_email=id).count() >= 1 or User.objects.filter(user_mobile_number=id).count()>=1:
        user =  User.objects.filter(user_email=id) or User.objects.filter(user_mobile_number=id)
        if user[0].is_verify is True:

       
         if(check_password(password,user[0].user_password)):
             token =get_tokens_for_user(user[0])
             Response.status_code = status.HTTP_200_OK
             return Response({
              'status code': status.HTTP_200_OK,
              'message':"user logged in successfully",
              'user id': user[0].user_id,
              'user_role': user[0].user_role,
              'token': token
                             })
         else:
             Response.status_code = status.HTTP_400_BAD_REQUEST
             return Response({'status': status.HTTP_400_BAD_REQUEST,
                              'message':"invalid password"
                              })
             
        else:
                 Response.status_code = status.HTTP_400_BAD_REQUEST
                 return Response({'status': status.HTTP_400_BAD_REQUEST,
                              'message':"user is not verified first verify yor account"
                              })
      else:
          Response.status_code = status.HTTP_400_BAD_REQUEST
          return Response({
              'status code': status.HTTP_400_BAD_REQUEST,
              'message':"user is not registered with this email or mobile number"         
               })
