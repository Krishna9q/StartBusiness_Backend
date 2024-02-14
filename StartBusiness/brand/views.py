from rest_framework import generics
from brand.models import Brand
from brand.serializers import BrandSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

# add brand
class BrandAddView(generics.GenericAPIView):
    serializer_class = BrandSerializer
    def post(self , request):
        if Brand.objects.filter(brand_name=request.data.get('brand_name')).count() >=1 :
            return Response({"error":"Brand already exists"},status=400)
        else:
            serializer = BrandSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response({
            "status" :"success",
            "message":"Brand is added successfully",
            }, status=201
            )


# get all brands and get one brand by id

class BrandView(APIView):
    def get(self, request, input=None, format=None):
        _id = input
        print(_id)
        if _id is not None:
            if Brand.objects.filter(brand_id=_id).count() > 0:
                brand  = Brand.objects.get(brand_id=_id)
                serializer = BrandSerializer(brand)


                return Response(
                    {
                        'status': 'success',
                        'message': "brand " + 'data retrieved successfully',
                        'data': serializer.data,
                    }, status=200
                )
            else:
             
                return Response(
                    {
                        'status':  'error',
                        'message': "brand not found",
                    },
                    status=404
                )
        else:
            brand = Brand.objects.all()    
            serializer = BrandSerializer(brand, many=True)
            return Response({
                 'status': 'success',
                 'message': "brand " + 'data retrieved successfully',
                 'data': serializer.data,
            }, status=200)
    
# update brand
class UpdateBrandView(APIView):
    def patch(self, request, input, format=None):
        _id = input
        print(_id)
        brand = Brand.objects.get(brand_id=_id)
        serializer = BrandSerializer(brand, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        if _id is not None:
            serializer.save()
            return Response({
             'status': 'success',
             'message': "brand updated successfully"
        },status=200)
        else:
            return Response({
                'status':'brand id not found'
        },status=404)
     
       
# delete brand
class DeleteBrandView(APIView):
    def delete(self, request, input, format=None):
        _id = input
        brand = Brand.objects.get(brand_id=_id)
        if _id is not None:
            brand.delete()
            return Response({
            'status': 'success',
            'message': "brand deleted successfully"
        }, status=200)
        else:
            return Response({
                'status': 'failure',
                'message': "No such brand id exists for delete."
                }, status=404)
    


