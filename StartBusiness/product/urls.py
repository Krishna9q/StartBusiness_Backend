from django.urls import path, include
from .views import *

urlpatterns = [
    path('add', ProductRegisterView.as_view(),name="add"),
    path('view/', ProductView.as_view(), name = 'manager view'),
    path('view/<uuid:input>/', ProductView.as_view(), name = 'manager view by id'),
    path('update/<uuid:input>/',UpdateProductView.as_view(),name="update manager by id"),
    path('delete/<uuid:input>/',DeleteProductView.as_view() ,name='delete manager by id'),
    path('pricing/<uuid:input>/',PricingView.as_view() ,name='delete manager by id'),
    path('otherDetails/<uuid:input>/',ProductDetailsView.as_view() ,name='delete manager by id')
    
    
]