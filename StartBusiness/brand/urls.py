from django.urls import path, include
from brand.views import *

urlpatterns = [
    path('add/',BrandAddView.as_view(),name="brand add"),
    path('view/',BrandView.as_view(),name='view brand'),
    path('view/<uuid:input>/', BrandView.as_view(), name = 'brand view by id'),
    path('update/<uuid:input>/',UpdateBrandView.as_view(),name="update manager by id"),
    path('delete/<uuid:input>/',DeleteBrandView.as_view() ,name='delete manager by id')
]