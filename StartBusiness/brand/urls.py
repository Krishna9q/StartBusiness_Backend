from django.urls import path, include
from brand.views import BrandAddView,UpdateBrandView,DeleteBrandView,BrandAllView,DealerViewAccordingBrand,BrandView

urlpatterns = [
    path('add/',BrandAddView.as_view(),name="brand add"),
    path('view/',BrandAllView.as_view(),name='view brand'),
    path('view/<uuid:input>/', BrandView.as_view(), name = 'brand view by id'),
    path('update/<uuid:input>/',UpdateBrandView.as_view(),name="update manager by id"),
    path('delete/<uuid:input>/',DeleteBrandView.as_view() ,name='delete manager by id'),
    path('dealer-view-according-to-brand/',DealerViewAccordingBrand.as_view(),name="brand add"),
]