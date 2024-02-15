from django.urls import path
from .views import *


urlpatterns = [
    path('register',CategoryRegisterView.as_view(), name = 'category register'),
    path('view',CategoryView.as_view(), name = 'category views'),
    path('view/<uuid:input>/',CategoryView.as_view(), name = 'category views single'),
    path('update/<uuid:input>/',CategoryUpdateView.as_view(), name = 'category update '),
    path('delete/<uuid:input>/',CategoryDeleteView.as_view(), name = 'category delete'),

]