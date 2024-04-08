from django.urls import path
from .views import *


urlpatterns = [
    path('add',ProductHighlightAddView.as_view(), name = 'product_highlight add'),
    path('view/',ProductHighlightAllView.as_view(), name = 'product_highlight views'),
    path('view/<uuid:input>/',ProductHighlightView.as_view(), name = 'product_highlight views single'),
    path('update/<uuid:input>/',ProductHighlightUpdateView.as_view(), name = 'product_highlight update '),
    path('delete/<uuid:input>',ProductHighlightDeleteView.as_view(), name = 'product_highlight delete'),

]