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
class userDetail(generics.RetrieveUpdateDestroyAPIView):
    #lookup_field = 'pk'
    queryset = User.objects.all()
    serializer_class = userSerializer
    
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
        # delete view for details
def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(GeeksModel, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")
 
    return render(request, "delete_view.html", context)

    '''
       
class orderxDetail(generics.ListCreateAPIView):
    #lookup_field = 'pk'
    queryset = order.objects.all()
    #permission_classes = (AllowAny,)
   
    serializer_class = orderxSerializer
    def perform_create(self, serializer):
        serializer.save() 
    def update(self,request, serializer,*args,**kwargs):
        instance = self.get_object()
        instance.sender = self.get_user()
        serializer = self.get_serializer(instance,data = request.data)
        self.perform_update(serializer)
        return Response(serializer.data)    
      
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
class restaurantList(generics.ListCreateAPIView):
    queryset = restaurant.objects.all()
    serializer_class = restaurantSerializer

    def perform_create(self, serializer):
        serializer.save()
class UpdateOrderView(generics.RetrieveUpdateDestroyAPIView,generics.UpdateAPIView):
    queryset = order2.objects.all()
    serializer_class = orderSerializer
    lookup_field = 'pk'
    permission_classes = (AllowAny,)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()#model
        serializer = self.get_serializer(instance, data=request.data)
        #print(serializer)
        

        if serializer.is_valid():
            #serializer1 = order2.objects.filter(pk=instance.pk).update(ordertrak='ready')
            #print(instance.ordertrak)
            #Survey.objects.filter(pk=survey.pk).update(active=True)
            #print(record)
            instance.save()
            serializer.save()
            
            return Response(serializer.data)
        
        else:
            print('not valid serilizer')
            return Response(serializer.data)
class orderDetail(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView,generics.UpdateAPIView):
    lookup_field = 'pk'
    queryset = order2.objects.all()
    permission_classes = (AllowAny,)
    
    print(queryset)
    serializer_class = orderSerializer
    
    def perform_create(self, serializer):
        #self.id   
        serializer.save() 
    def update(self, request, *args, **kwargs):
        instance = self.get_object()#model
        serializer = self.get_serializer(instance, data=request.data)
        #print(serializer)
        

        if serializer.is_valid():
            #serializer1 = order2.objects.filter(pk=instance.pk).update(ordertrak='ready')
            #print(instance.ordertrak)
            #Survey.objects.filter(pk=survey.pk).update(active=True)
            #print(record)
            instance.save()
            serializer.save()
            
            return Response(serializer.data)
        
        else:
            print('not valid serilizer')
            return Response(serializer.data)
        
        """'table': i['table'],
                                                        'food': i[
                                                            'food'], //list for food
                                                        'restaurantx':
                                                            i['restaurantx'],
                                                        'time': i['time'],
                                                        'owner': i['owner'],
                                                        //$sum
                                                        'totalprice':
                                                            i['totalprice'],
                                                        'ordertype':
                                                            i['ordertype'],
                                                        'ordername':
                                                            i['ordername'],
                                                        'ordertrak': 'ready',
                                                        'ordertime':
                                                            i['ordertime'],"""