from django.urls import path, include
from .views import *


urlpatterns = [
    path('register', ContractorRegistorView.as_view(), name = 'Contractor register'),
    path('view',ContractorView.as_view(), name = 'Contractor view'),
    path('view/<uuid:input>/',ContractorView.as_view(), name = 'Contractor view'),
    path('update/<uuid:input>/',ContractorUpdateView.as_view(), name = 'Contractor update'),
    path('delete/<uuid:input>/',ContratorDeleteView.as_view(), name = 'Contractor delete'),
]