from django.shortcuts import render
from rest_framework import generics
from category.serializers import CategorySerializer
from .models import Category
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

class CategoryRegisterView(generics.GenericAPIView):
    serializer_class = CategorySerializer
    def post(self, request,format=None):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'status':status.HTTP_201_CREATED,
            "msg":'Category Registered',
            'data': serializer.data
        },status=200)

class CategoryView(APIView):
    
    def get(self,request, input = None,format=None):
        id = input
        if id is not None:
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
        else:
            category = Category.objects.all()
            serializer = CategorySerializer(category, many=True)
           
            return Response({
             'status':status.HTTP_200_OK,
             'message': "Category data retrived",
             'data':serializer.data
            },status=200)
        
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