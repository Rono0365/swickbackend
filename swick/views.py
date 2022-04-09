from cgitb import lookup
from django.shortcuts import render
#from matplotlib.pyplot import table
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
# Create your views here.
class CustomAuthToken(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
class foodList(generics.ListCreateAPIView):
    queryset = food.objects.all()
    serializer_class = foodSerializer

    def perform_create(self, serializer):
        serializer.save()
class cartList(generics.ListCreateAPIView):
    queryset = Vcart.objects.all()
    serializer_class = cartSerializer

    def perform_create(self, serializer):
        serializer.save()

class tableList(generics.ListCreateAPIView):
    queryset = table.objects.all()
    serializer_class = tableSerializer

    def perform_create(self, serializer):
        serializer.save()
class tableDetail(generics.RetrieveUpdateDestroyAPIView):
    #lookup_field = 'pk'
    queryset = table.objects.all()
    serializer_class = tableSerializer
    
    #filter_fields = ('name')
    # inside OrganisationDetail
    #ueryset = table.objects.all()
    '''
    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        # make sure to catch 404's below
        obj = queryset.get(pk=self.request.user.table_id)
        self.check_object_permissions(self.request, obj)
        return obj
    '''
class orderDetail(generics.ListCreateAPIView):
    #lookup_field = 'pk'
    queryset = order2.objects.all()
    #permission_classes = (AllowAny,)
   
    serializer_class = orderSerializer
    def perform_create(self, serializer):
        serializer.save() 
class orderxDetail(generics.ListCreateAPIView):
    #lookup_field = 'pk'
    queryset = order.objects.all()
    #permission_classes = (AllowAny,)
   
    serializer_class = orderxSerializer
    def perform_create(self, serializer):
        serializer.save() 
      
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer          
class RestregisterView(generics.CreateAPIView):
    queryset = restaurant.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = restaurantSerializer      
class restaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    #lookup_field = 'pk'
    queryset = restaurant.objects.all()
    serializer_class = restaurantSerializer

