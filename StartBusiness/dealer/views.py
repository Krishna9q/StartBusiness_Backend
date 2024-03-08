from rest_framework.generics import GenericAPIView,ListAPIView
from dealer.filter import DealerFilter
from dealer.models import Dealer
from dealer.serializers import DealerSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from StartBusiness.s3_image_config import upload_base64_file
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend



# add dealer
class DealerAddView(GenericAPIView):
    serializer_class = DealerSerializer
    def post(self , request):
            serializer = DealerSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            file = request.data.get('dealer_image')
            data=upload_base64_file(file,'brand')
            serializer.validated_data['dealer_image']= data
            serializer.save()
         

            return Response({
            "status" :"success",
            "message":"Dealer is added successfully",
            }, status=201
            )

# get all dealer and get one dealer by id
class DealerAllView(ListAPIView):
    queryset = Dealer.objects.all()
    filter_backends = [DjangoFilterBackend]
    serializer_class = DealerSerializer
    filterset_class = DealerFilter
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response({
            'status':status.HTTP_200_OK,
            "message":'dealer data retrieved successfully ',
            'data':response.data
        },status=200)

# get one dealer by id
class DealerView(APIView):
    def get(self, request, input=None, format=None):
            _id = input
      
            if Dealer.objects.filter(dealer_id=_id).count() > 0:
                dealer  = Dealer.objects.get(dealer_id=_id)
                serializer = DealerSerializer(dealer)


                return Response(
                    {
                        'status': 'success',
                        'message': "dealer " + 'data retrieved successfully',
                        'data': serializer.data,
                    }, status=status.HTTP_200_OK
                )
            else:
             
                return Response(
                    {
                        'status':  'error',
                        'message': "dealer not found",
                    },
                    status=status.HTTP_404_NOT_FOUND
                )   

# update dealer
class UpdateDealerView(APIView):
    def patch(self, request, input, format=None):
      _id = input
      if _id is not None: 
        dealer = Dealer.objects.get(dealer_id=_id)
        serializer = DealerSerializer(dealer, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        if(request.data.get('dealer_image')is not None):
            file = request.data.get('dealer_image')
            data=upload_base64_file(file,'brand')
            serializer.validated_data['dealer_image']= data
        serializer.save()
        return Response({
             'status': 'success',
             'message': "dealer updated successfully"
        },status=200)
      else:
            return Response({
                'status':'dealer id not found'
        },status=404)
     
       
# delete dealer
class DeleteDealerView(APIView):
    def delete(self, request, input, format=None):
        _id = input
        dealer = Dealer.objects.get(dealer_id=_id)
        if _id is not None:
            dealer.delete()
            return Response({
            'status': 'success',
            'message': "dealer deleted successfully"
        }, status=200)
        else:
            return Response({
                'status': 'failure',
                'message': "No such dealer id exists for delete."
                }, status=404)
    



