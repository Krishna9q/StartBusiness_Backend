from django.shortcuts import render
from rest_framework.generics import GenericAPIView , ListAPIView
from category.serializers import CategorySerializer
from .models import Category
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from StartBusiness.custom_paginations import CustomPagination
from rest_framework.filters import OrderingFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from StartBusiness.s3_image_config import upload_base64_file

class CategoryRegisterView(GenericAPIView):
  
    serializer_class = CategorySerializer
    def post(self, request,format=None):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = request.data.get('category_image')
        data=upload_base64_file(file,'category/')
        serializer.validated_data['category_image']= data
        serializer.save()

        return Response({
            'status':status.HTTP_201_CREATED,
            "msg":'Category Registered',
            'data': serializer.data
        },status=200)

class CategoryView(ListAPIView):
   queryset = Category.objects.all().order_by('created_at')
   serializer_class = CategorySerializer
   pagination_class = CustomPagination
   
   def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
 
           
        return Response(
               {
                  'status': status.HTTP_200_OK,
                  'message': 'Category data retrieved successfully',
                  'data': response.data
               },status=200
            )
class CategoryViewById(APIView):
    
    def get(self,request, input = None,format=None):
        id = input
        
        if Category.objects.filter(category_id=id).count()>=1:
            category = Category.objects.get(category_id=id)
            serializer = CategorySerializer(category)
            return Response({
                'status':status.HTTP_200_OK,
                'message': "Category data retrived",
                'data':serializer.data
            },status=200)
        else:
            return Response({
                'status':status.HTTP_400_BAD_REQUEST,
                'message': "Invalid Category id"
            },
            status=400)
       
        
class CategoryUpdateView(APIView):
    serialier_class = CategorySerializer
    def patch(self, request, input, format=None):
        id = input
        if Category.objects.filter(category_id=id).count() >=1:
           category = Category.objects.get(category_id=id)
           serializer = CategorySerializer(category, data=request.data, partial=True)
           serializer.is_valid(raise_exception=True)
           serializer.save()

           return Response({
                'status': status.HTTP_200_OK,
                'data': serializer.data,
                'message': 'Contractor Updated Successfully'  
                },status=200)
        else:
            return Response({
               'status': status.HTTP_400_BAD_REQUEST,
                'message': 'invalid id',
                },
                status=400)
        

class CategoryDeleteView(APIView):
    def delete(self, request, input):
        id = input
        if Category.objects.filter(category_id=id).count() >= 1:
            category = Category.objects.get(category_id=id)
            category.delete()
            return Response({
            'status': status.HTTP_200_OK,
             'message': 'Category Deleted Successfully' 
            },
            status=200)
        
        else:
            return Response({
             'status': status.HTTP_400_BAD_REQUEST,
             'message': 'invalid Category_id',
            },
            status=400)
        

        