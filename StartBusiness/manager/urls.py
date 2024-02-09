from django.urls import path, include
from manager.views import *

urlpatterns = [
    path('register',ManagerRegisterView.as_view(),name="hello"),
    path('view/', ManagerView.as_view(), name = 'manager view'),
    path('view/<uuid:input>/', ManagerView.as_view(), name = 'manager view by id'),
    path('update/<uuid:input>/',UpdateManagerView.as_view(),name="update manager by id"),
    path('delete/<uuid:input>/',DeleteManagerView.as_view() ,name='delete manager by id')
    

   

    
]
