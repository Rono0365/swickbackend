from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class foodSerializer(serializers.ModelSerializer):
    class Meta:
        model = food
        fields = ['name','price','count','image_url']
class cartSerializer(serializers.ModelSerializer):
    food = foodSerializer(many=True)
    class Meta:
        model = Vcart
        fields = ['count','food']
       
class categorySerializer(serializers.ModelSerializer):
    food = foodSerializer(many=True)
    class Meta:
        model =  category
        fields = ['name','caption','food']        
class menuSerializer(serializers.ModelSerializer):
    menu = categorySerializer(many=True)
    class Meta:
        model =  Menu
        fields = ['menu']

class tableSerializer(serializers.ModelSerializer):
    #restaurant = serializers.ReadOnlyField(source='restaurant.name')
    menu = menuSerializer(many=True)
    #order = foodSerializer(many=True)
    class Meta:
         model = table
         fields = ['name','menu']

class orderSerializer(serializers.ModelSerializer):
    #food = foodSerializer(many=True)
    #table = serializers.ReadOnlyField(source='order2.id')
    #add table nameUnsupported Media Type: /order2/
    #username = serializers.ReadOnlyField(source='owner.username')#owner.username
    #lastname = serializers.ReadOnlyField(source='owner.last_name')
    #orderxx = serializers.PrimaryKeyRelatedField(queryset=order2.objects.all())
    orderxx = serializers.ReadOnlyField(source='order2.id')
    
    class Meta:
        model = order2
        fields = ['orderxx','table','food','owner','restaurantx','time','totalprice','ordertype','ordername','ordertrak','ordertime']#,'customer' 
class restaurantSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='username.username')
    
    menu = menuSerializer(many=True)
    orders = orderSerializer(many=True)
    #'namer'
    class Meta:
        model =  restaurant
        fields = ['location','city','orders','menu','username','image_of_restaurant']                

class orderxSerializer(serializers.ModelSerializer):
    #food = foodSerializer(many=True)
    #table = serializers.ReadOnlyField(source='table.name')
    #add table nameUnsupported Media Type: /order2/
    
    class Meta:
        model = order
        fields = ['food']#,'customer' 

class RegisterSerializer(serializers.ModelSerializer,):
    permission_classes = []
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user        