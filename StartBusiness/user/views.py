from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from user.serializers import UserSerializer
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from user.models import User

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
