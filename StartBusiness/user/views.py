from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from user.serializers import UserLoginSerializer, UserSerializer
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password , check_password
from user.models import User
from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'access': str(refresh.access_token),
        'refresh': str(refresh)
    }

class UserRegisterView(GenericAPIView):
    serializer_class = UserSerializer
    def post(self, request , format=None):
    
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.validated_data['user_password']=make_password(serializer.validated_data['user_password'])
        serializer.save()
        return Response({
                 'status': status.HTTP_200_OK
                                   })
        



class UserView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, input=None, format=None):
        id = input
        if id is not None:
            if User.objects.filter(user_id=id).count() >= 1:
                user  = User.objects.get(user_id=id)
                serializer = UserSerializer(user)
              
              
                return Response(
                    {
                        'status': status.HTTP_200_OK,
                        'message': "user " + 'data retrieved successfully',
                        'data': serializer.data,
                    }
                )
            else:
             
                return Response(
                    {
                        'status': status.HTTP_400_BAD_REQUEST,
                        'message': "Invalid user id",
                    },
                )
        else:
            user = User.objects.all()    
            serializer = UserSerializer(user, many=True)
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
             return Response({
              'status code': status.HTTP_200_OK,
              'message':"user logged in successfully",
              'user id': user[0].user_id,
              'user_role': user[0].user_role,
              'token': token
                             })
         else:
             return Response({'status': status.HTTP_400_BAD_REQUEST,
                              'message':"invalid password"
                              })
             
        else:
                 return Response({'status': status.HTTP_400_BAD_REQUEST,
                              'message':"user is not verified first verify yor account"
                              })
      else:
          return Response({
              'status code': status.HTTP_400_BAD_REQUEST,
              'message':"user is not registered with this email or mobile number"         
               })
