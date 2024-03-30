from django.urls import path
from .views import *


urlpatterns = [
    path('add',StockAddView.as_view(), name = 'stock add'),
    path('view/',StockView.as_view(), name = 'stock views'),
    path('view/<uuid:input>/',StockView.as_view(), name = 'stock views single'),
    path('update/<uuid:input>/',StockUpdateView.as_view(), name = 'stock update '),
    path('delete/<uuid:input>',StockDeleteView.as_view(), name = 'stock delete'),

]