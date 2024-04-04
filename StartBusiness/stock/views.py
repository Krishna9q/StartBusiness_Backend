from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from django.core.exceptions import ObjectDoesNotExist
from stock.models import Stock
from stock.serializers import StockSerializer

# add stock
class StockAddView(GenericAPIView):
    serializer_class = StockSerializer
    def post(self, request,format=None):
        serializer = StockSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'status':status.HTTP_201_CREATED,
            "msg":'Stock added successfully'
        },status=201)


# update stock
class StockUpdateView(GenericAPIView):
    serializer_class = StockSerializer
    def patch(self, request, input):
        id = input
        try:
           stock = Stock.objects.get(stock_id=id)
           serializer = StockSerializer(stock, data=request.data, partial=True)
           serializer.is_valid(raise_exception=True)
           serializer.save()
           return Response({
                'status': status.HTTP_200_OK,
                'message': 'Stock Updated Successfully'  
                },status=200)
        except ObjectDoesNotExist:
            return Response({
               'status': status.HTTP_400_BAD_REQUEST,
                'message': 'invalid stock_id',
                },
                status=400)

# get stock or get stock by id   
class StockView(APIView):
    serializer_class = StockSerializer
    def get(self, request, input=None, format=None):
        _id = input
        print(_id)
        if _id is not None:
            try:
                stock  = Stock.objects.get(stock_id=_id)
                serializer = StockSerializer(stock)
                return Response(
                    {
                        'status': 'success',
                        'message': 'stock data retrieved successfully',
                        'data': serializer.data,
                    }, status=200
                )
            except ObjectDoesNotExist:
                return Response(
                    {
                        'status':  'error',
                        'message': "stock data not found",
                    },
                    status=404
                )
        else:
            stock = Stock.objects.all()
            serializer = StockSerializer(stock, many=True)
            return Response({
                 'status': 'success',
                 'message': 'stock data retrieved successfully',
                 'data': serializer.data,
            }, status=200)
        

# delete stock
class StockDeleteView(APIView):
    def delete(self, request, input):
        try:
            id = input
            stock = Stock.objects.get(stock_id=id)
            stock.delete()
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Stock Deleted Successfully'
            })
        except ObjectDoesNotExist:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Invalid stock_id'
            }, status=status.HTTP_400_BAD_REQUEST)
