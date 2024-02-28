from rest_framework.generics import GenericAPIView
from dealer.models import Dealer
from dealer.serializers import DealerSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from StartBusiness.s3_image_config import upload_base64_file
from rest_framework import status

# add dealer
class DealerAddView(GenericAPIView):
    serializer_class = DealerSerializer
    def post(self , request):
        if Dealer.objects.filter(dealer_email=request.data.get('dealer_email')).count() >=1 or Dealer.objects.filter(dealer_mobile_number=request.data.get('dealer_mobile_number')).count() >=1:
          
              return Response({
                                  'status' : status.HTTP_400_BAD_REQUEST,
                                   'message' : "this user is already registerd"
                      },status=400)
        else:
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

class DealerView(APIView):
    def get(self, request, input=None, format=None):
        _id = input
        print(_id)
        if _id is not None:
            if Dealer.objects.filter(dealer_id=_id).count() > 0:
                dealer  = Dealer.objects.get(dealer_id=_id)
                serializer = DealerSerializer(dealer)


                return Response(
                    {
                        'status': 'success',
                        'message': "dealer " + 'data retrieved successfully',
                        'data': serializer.data,
                    }, status=200
                )
            else:
             
                return Response(
                    {
                        'status':  'error',
                        'message': "dealer not found",
                    },
                    status=404
                )
        else:
            dealer = Dealer.objects.all()    
            serializer = DealerSerializer(dealer, many=True)
            return Response({
                 'status': 'success',
                 'message': "dealer " + 'data retrieved successfully',
                 'data': serializer.data,
            }, status=200)
    
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
    



