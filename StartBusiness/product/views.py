from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from product.serializers import *
from .models import Product

# register 01
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

# View Product Full
class ProductView(APIView):
    def get(self, request, input=None, format=None):
        _id = input
        print(_id)
        if _id is not None:
            if Product.objects.filter(product_id=_id).count() > 0:
                product  = Product.objects.get(product_id=_id)
                serializer = ProductFullDetailsSerializer(product)


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
            serializer = ProductFullDetailsSerializer(product, many=True)
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
    

# Other ----------------------------------------------------------

   # Pricing View
class PricingView(GenericAPIView):
    serializer_class = ProductPricingSerializer
    def patch(self,request ,input):
        _id = input
        print(_id)
        product = Product.objects.get(product_id=_id)
        serializer = ProductPricingSerializer(product, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        if _id is not None:
            serializer.save()
            return Response({
             'status': 'success',
             'message': "Pricing updated successfully"
        },status=200)
        else:
            return Response({
                'status':'Product id not found'
        },status=404)
    

# Product Details View
class ProductDetailsView(GenericAPIView):
    serializer_class = ProductDetailsSerializer
    def patch(self,request ,input):
        _id = input
        print(_id)
        product = Product.objects.get(product_id=_id)
        serializer = ProductDetailsSerializer(product, data=request.data, partial=True)
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
    

    # Inventory View
class InventoryView(GenericAPIView):
    serializer_class = ProductInventorySerializer
    def patch(self,request ,input):
        _id = input
        print(_id)
        product = Product.objects.get(product_id=_id)
        serializer = ProductInventorySerializer(product, data=request.data, partial=True)
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
    
    # ProductVisuals View
class ProductVisualsView(GenericAPIView):
    serializer_class = ProductVisualsSerializer
    def patch(self,request ,input):
        _id = input
        print(_id)
        product = Product.objects.get(product_id=_id)
        serializer = ProductVisualsSerializer(product, data=request.data, partial=True)
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
    

    # Product Shipping Information View
class ProductShippingInformationView(GenericAPIView):
    serializer_class = ProductShippingInformationSerializer
    def patch(self,request ,input):
        _id = input
        print(_id)
        product = Product.objects.get(product_id=_id)
        serializer = ProductShippingInformationSerializer(product, data=request.data, partial=True)
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
    
    # Product tags View
class ProducttagView(GenericAPIView):
    serializer_class = ProducttagsSerializer
    def patch(self,request ,input):
        _id = input
        print(_id)
        product = Product.objects.get(product_id=_id)
        serializer = ProducttagsSerializer(product, data=request.data, partial=True)
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
    
    # Product Feature View
class ProductFeatureView(GenericAPIView):
    serializer_class = ProductFeaturedSerializer
    def patch(self,request ,input):
        _id = input
        print(_id)
        product = Product.objects.get(product_id=_id)
        serializer = ProductFeaturedSerializer(product, data=request.data, partial=True)
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
    
    # Product Specifications View
class ProductSpecificationsView(GenericAPIView):
    serializer_class = ProductSpecificationsSerializer
    def patch(self,request ,input):
        _id = input
        print(_id)
        product = Product.objects.get(product_id=_id)
        serializer = ProductSpecificationsSerializer(product, data=request.data, partial=True)
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
    

    # Product TaxInformation View
class ProductTaxInformationView(GenericAPIView):
    serializer_class = ProductTaxInformationSerializer
    def patch(self,request ,input):
        _id = input
        print(_id)
        product = Product.objects.get(product_id=_id)
        serializer = ProductTaxInformationSerializer(product, data=request.data, partial=True)
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
    

    # Product Variants View
class ProductVariantsView(GenericAPIView):
    serializer_class = ProductVariantsSerializer
    def patch(self,request ,input):
        _id = input
        print(_id)
        product = Product.objects.get(product_id=_id)
        serializer = ProductVariantsSerializer(product, data=request.data, partial=True)
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
    
    # ProductBulkPricing View
class ProductBulkPricingView(GenericAPIView):
    serializer_class = BulkPricingSerializer
    def patch(self,request ,input):
        _id = input
        print(_id)
        product = Product.objects.get(product_id=_id)
        serializer = BulkPricingSerializer(product, data=request.data, partial=True)
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
    
    # Product Sales Information View
class ProductSalesInformationView(GenericAPIView):
    serializer_class = SalesInformationSerializer
    def patch(self,request ,input):
        _id = input
        print(_id)
        product = Product.objects.get(product_id=_id)
        serializer = SalesInformationSerializer(product, data=request.data, partial=True)
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
    
  
    # Product CustomizationOptions View
class ProductCustomizationOptionsView(GenericAPIView):
    serializer_class = CustomizationOptionsSerializer
    def patch(self,request ,input):
        _id = input
        print(_id)
        product = Product.objects.get(product_id=_id)
        serializer = CustomizationOptionsSerializer(product, data=request.data, partial=True)
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
    
  
    # Product Review View
class ProductReviewView(GenericAPIView):
    serializer_class = ProductReviewsSerializer
    def patch(self,request ,input):
        _id = input
        print(_id)
        product = Product.objects.get(product_id=_id)
        serializer = ProductReviewsSerializer(product, data=request.data, partial=True)
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
    
  
    # Product ReturnPolicy View
class ProductReturnPolicyView(GenericAPIView):
    serializer_class = ReturnPolicySerializer
    def patch(self,request ,input):
        _id = input
        print(_id)
        product = Product.objects.get(product_id=_id)
        serializer = ReturnPolicySerializer(product, data=request.data, partial=True)
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
    
  
    # Product SaleHistory View
class ProductSaleHistoryView(GenericAPIView):
    serializer_class = SalesHistorySerializer
    def patch(self,request ,input):
        _id = input
        print(_id)
        product = Product.objects.get(product_id=_id)
        serializer = SalesHistorySerializer(product, data=request.data, partial=True)
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
    

  
    # Product Status View
class ProductStatusView(GenericAPIView):
    serializer_class = ProductStatusSerializer
    def patch(self,request ,input):
        _id = input
        print(_id)
        product = Product.objects.get(product_id=_id)
        serializer = ProductStatusSerializer(product, data=request.data, partial=True)
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
    

    # Product Status View
class ProductAdminNotesView(GenericAPIView):
    serializer_class = AdminNotesSerializer
    def patch(self,request ,input):
        _id = input
        print(_id)
        product = Product.objects.get(product_id=_id)
        serializer = AdminNotesSerializer(product, data=request.data, partial=True)
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
    

    
    # Product Status View
class ProductDateAddedView(GenericAPIView):
    serializer_class = DateAddedSerializer
    def patch(self,request ,input):
        _id = input
        print(_id)
        product = Product.objects.get(product_id=_id)
        serializer = DateAddedSerializer(product, data=request.data, partial=True)
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
    

    
    # Product Status View
class ProductLastModifiedView(GenericAPIView):
    serializer_class = LastModifiedSerializer
    def patch(self,request ,input):
        _id = input
        print(_id)
        product = Product.objects.get(product_id=_id)
        serializer = LastModifiedSerializer(product, data=request.data, partial=True)
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
    


    
    # Product Status View
class ProductUserAssignedView(GenericAPIView):
    serializer_class = UserAssignedSerializer
    def patch(self,request ,input):
        _id = input
        print(_id)
        product = Product.objects.get(product_id=_id)
        serializer = UserAssignedSerializer(product, data=request.data, partial=True)
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
    


    
    # Product Status View
class ProductApprovalStatusView(GenericAPIView):
    serializer_class = ProductStatusSerializer
    def patch(self,request ,input):
        _id = input
        print(_id)
        product = Product.objects.get(product_id=_id)
        serializer = ProductStatusSerializer(product, data=request.data, partial=True)
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
    


    
    # Product Status View
class ProductInternalProducIDView(GenericAPIView):
    serializer_class = InternalProductIDSerializer
    def patch(self,request ,input):
        _id = input
        print(_id)
        product = Product.objects.get(product_id=_id)
        serializer = InternalProductIDSerializer(product, data=request.data, partial=True)
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
    


    
    # Product Status View
class ProductSalesRepresentativeView(GenericAPIView):
    serializer_class = SalesRepresentativeSerializer
    def patch(self,request ,input):
        _id = input
        print(_id)
        product = Product.objects.get(product_id=_id)
        serializer = SalesRepresentativeSerializer(product, data=request.data, partial=True)
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
    
    # Product Status View
class ProductURIView(GenericAPIView):
    serializer_class = ProductURLSerializer
    def patch(self,request ,input):
        _id = input
        print(_id)
        product = Product.objects.get(product_id=_id)
        serializer = ProductURLSerializer(product, data=request.data, partial=True)
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
    
    # Product Status View
class ProductNotificationPreferenceView(GenericAPIView):
    serializer_class = NotificationPreferencesSerializer
    def patch(self,request ,input):
        _id = input
        print(_id)
        product = Product.objects.get(product_id=_id)
        serializer = NotificationPreferencesSerializer(product, data=request.data, partial=True)
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
    
    # Product Status View
class ProductAuditTrailView(GenericAPIView):
    serializer_class = AuditTrailSerializer
    def patch(self,request ,input):
        _id = input
        print(_id)
        product = Product.objects.get(product_id=_id)
        serializer = AuditTrailSerializer(product, data=request.data, partial=True)
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
    