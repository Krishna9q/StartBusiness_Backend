from django.urls import path, include
from .views import *


urlpatterns = [
    path('register', UserRegisterView.as_view(), name = 'user register'),
    path('view/', UserView.as_view(), name = 'user view'),
    path('view/<uuid:input>/', UserView.as_view(), name = 'user view by id'),
    path('update/<uuid:input>/', UserUpdateView.as_view(), name = 'user update'),
  
]