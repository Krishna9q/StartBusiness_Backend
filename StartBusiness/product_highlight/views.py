from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from product_highlight.models import ProductHighlight
from product_highlight.serializers import ProductHighlightSerializer
from django.core.exceptions import ObjectDoesNotExist

# add product highlight
class ProductHighlightAddView(GenericAPIView):
    serializer_class = ProductHighlightSerializer
    def post(self, request,format=None):
        serializer = ProductHighlightSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'status':status.HTTP_201_CREATED,
            "msg":'Product Highlight Registered'
        },status=201)


# update product highlight
class ProductHighlightUpdateView(GenericAPIView):
    serialier_class = ProductHighlightSerializer
    def patch(self, request, input, format=None):
        id = input
        try:
           product_highlight = ProductHighlight.objects.get(product=id)
           serializer = ProductHighlightSerializer(product_highlight, data=request.data, partial=True)
           serializer.is_valid(raise_exception=True)
           serializer.save()

           return Response({
                'status': status.HTTP_200_OK,
                'message': 'Product Highlight Updated Successfully'  
                },status=200)
        except ObjectDoesNotExist:
            return Response({
               'status': status.HTTP_400_BAD_REQUEST,
                'message': 'invalid_id',
                },
                status=400)

# get product highlight or get product highlight by id   
class ProductHighlightView(APIView):
    serializer_class = ProductHighlightSerializer
    def get(self, request, input=None, format=None):
        _id = input
        print(_id)
        if _id is not None:
            try:
                product_highlight  = ProductHighlight.objects.get(product=_id)
                serializer = ProductHighlightSerializer(product_highlight)
                return Response(
                    {
                        'status': 'success',
                        'message': 'product_highlight data retrieved successfully',
                        'data': serializer.data,
                    }, status=200
                )
            except ObjectDoesNotExist:
                return Response(
                    {
                        'status':  'error',
                        'message': "Product highlight not found",
                    },
                    status=404
                )
        else:
            product_highlight = ProductHighlight.objects.all()
            serializer = ProductHighlightSerializer(product_highlight, many=True)
            return Response({
                 'status': 'success',
                 'message': 'product_highlight data retrieved successfully',
                 'data': serializer.data,
            }, status=200)
        

# delete product highlight
class ProductHighlightDeleteView(APIView):
    def delete(self, request, input):
        try:
            id = input
            product_highlight = ProductHighlight.objects.get(product_highlight_id=id)
            product_highlight.delete()
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Product Highlight Deleted Successfully'
            })
        except ObjectDoesNotExist:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Invalid product_highlight_id'
            }, status=status.HTTP_400_BAD_REQUEST)