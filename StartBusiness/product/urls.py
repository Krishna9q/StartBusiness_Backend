from django.urls import path, include
from product.views import *

urlpatterns = [
    path('add/',ProductAddView.as_view(),name="dealer add"),
    # path('view/',DealerAllView.as_view(),name='view dealer'),
    # path('view/<uuid:input>/', DealerView.as_view(), name = 'dealer view by id'),
    # path('update/<uuid:input>/',UpdateDealerView.as_view(),name="update dealer by id"),
    # path('delete/<uuid:input>/',DeleteDealerView.as_view() ,name='delete dealer by id')
]