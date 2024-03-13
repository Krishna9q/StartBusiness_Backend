from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from product.serializers import ProductSerializer
from .models import Product

class ProductRegisterView(GenericAPIView):
    serializer_class = ProductSerializer
    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "status" :"success",
            "message":"Product is added successfully",
            "data":serializer.data
            }, status=201

        )
    
class OtherDetailsView(GenericAPIView):
    # serializer_class = OtherSerializer
    # def post(self,request ,input):
    #     _id = input
    #     print(_id)
    #     product = Product.objects.get(product_id=_id)
    #     serializer = OtherSerializer(product, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     if _id is not None:
    #         serializer.save()
    #         return Response({
    #          'status': 'success',
    #          'message': "Product updated successfully"
    #     },status=200)
    #     else:
    #         return Response({
    #             'status':'Product id not found'
    #     },status=404)
    pass 


        
    
class ProductView(APIView):
    def get(self, request, input=None, format=None):
        _id = input
        print(_id)
        if _id is not None:
            if Product.objects.filter(product_id=_id).count() > 0:
                product  = Product.objects.get(product_id=_id)
                serializer = ProductSerializer(product)


                return Response(
                    {
                        'status': 'success',
                        'message': "Product " + 'data retrieved successfully',
                        'data': serializer.data,
                    }, status=200
                )
            else:
             
                return Response(
                    {
                        'status':  'error',
                        'message': "Product not found",
                    },
                    status=404
                )
        else:
            product = Product.objects.all()    
            serializer = ProductSerializer(product, many=True)
            return Response({
                 'status': 'success',
                 'message': "  " + 'data retrieved successfully',
                 'data': serializer.data,
            }, status=200)
    

class UpdateProductView(APIView):
    def patch(self, request, input, format=None):
        _id = input
        print(_id)
        product = Product.objects.get(product_id=_id)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        if _id is not None:
            serializer.save()
            return Response({
             'status': 'success',
             'message': "Product updated successfully"
        },status=200)
        else:
            return Response({
                'status':'Product id not found'
        },status=404)
     
       

class DeleteProductView(APIView):
    def delete(self, request, input, format=None):
        _id = input
        product = Product.objects.get(product_id=_id)
        if _id is not None:
            product.delete()
            return Response({
            'status': 'success',
            'message': "Product deleted successfully"
        }, status=200)
        else:
            return Response({
                'status': 'failure',
                'message': "No such Product id exists for delete."
                }, status=404)
    

class productvideoUpload(GenericAPIView):
    serializer_class = ProductSerializer
    def post(self, request, input, format=None):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'status':'success',
            'message': "Product uploaded successfully"

        },status=200)