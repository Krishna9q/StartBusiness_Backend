from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from product.serializers import ProductVideoSerializers
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class ProductAddView(GenericAPIView):
    serializer_class = ProductVideoSerializers
    def post(self , request):
            serializer = ProductVideoSerializers(data=request.data)
            serializer.is_valid(raise_exception=True)
           
            serializer.save()

            return Response({
            "status" :"success",
            "message":"Brand is added successfully",
            }, status=status.HTTP_201_CREATED
            )