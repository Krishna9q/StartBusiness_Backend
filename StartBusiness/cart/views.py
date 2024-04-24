from cart.filter import CartFilter
from cart.models import Cart
from cart.serializers import CartSerializer,CartViewSerializer,CartUpdateSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView , ListAPIView
from rest_framework.views import APIView


class CartRegisterView(GenericAPIView):
    serializer_class = CartSerializer
    def post(self, request,format=None):
        serializer = CartSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'status':status.HTTP_201_CREATED,
            "msg":'Cart Registered',
        },status=201)

class CartView(ListAPIView):
   queryset = Cart.objects.all()
   serializer_class = CartViewSerializer
   filterset_class = CartFilter
   
   def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        if response.data == []:
            return Response({
                "message":"No Data Found!!"
            })
        return Response(
               {
                  'status': status.HTTP_200_OK,
                  'message': 'Cart data retrieved successfully',
                  'data': response.data
               },status=200
            )
class CartViewById(APIView):
    
    def get(self,request, input = None,format=None):
        _id = input
        try:
            cart = Cart.objects.get(cart_id=_id)
            serializer = CartSerializer(cart)
            return Response({
                'status':status.HTTP_200_OK,
                'message': "Cart data retrived",
                'data':serializer.data
            },status=200)
        except Cart.DoesNotExist:
            return Response({
                'status':status.HTTP_404_NOT_FOUND,
                'message': "Invalid Cart id"
            },
            status=400)
       
        
class CartUpdateView(GenericAPIView):
    serializer_class = CartUpdateSerializer
    def patch(self, request, input, format=None):
        _id = input
        try:
           cart = Cart.objects.get(cart_id=_id)
           serializer = CartUpdateSerializer(cart, data=request.data, partial=True)
           serializer.is_valid(raise_exception=True)
           serializer.save()
           return Response({
                'status': status.HTTP_200_OK,
                'message': 'Cart Updated Successfully'  
                },status=200)
        except Cart.DoesNotExist:
            return Response({
               'status': status.HTTP_404_NOT_FOUND,
                'message': 'invalid id',
                },
                status=400)
        

class CartDeleteView(APIView):
    def delete(self, request, input):
        _id = input
        try:
            cart = Cart.objects.get(cart_id=_id)
            cart.delete()
            return Response({
            'status': status.HTTP_200_OK,
             'message': 'Cart Deleted Successfully' 
            },
            status=200)
        except Cart.DoesNotExist:
            return Response({
             'status': status.HTTP_404_NOT_FOUND,
             'message': 'invalid Cart_id',
            },
            status=400)
