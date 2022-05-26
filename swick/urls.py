from django.urls import path
from rest_framework import urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('restaurant/', restaurantList.as_view()),
    path('restaurant/<int:pk>/', restaurantDetail.as_view()),
    
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('me/<int:pk>/', userDetail.as_view()),

    #path('tables/', tableList.as_view()),
    #path('table/<int:year>/<slug:slug>/', tableDetail.as_view()),
    path('table/<int:pk>/', tableDetail.as_view()),
    #name='article_detail'),
    path('orderx/', UpdateOrderView.as_view()),
    path('cart/', cartList.as_view()),
    
    path('food/', foodList.as_view()),
    path('order/', orderDetail.as_view()),
    path('order/<int:pk>/', UpdateOrderView.as_view()),
]
