from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
#from django.contrib.auth.models import User

class food(models.Model):
    name = models.CharField(max_length=100,default='')
    price = models.CharField(max_length=100,default='')
    count = models.CharField(max_length=100,default='1')
    image_url = models.CharField(max_length=10000,default='')

class category(models.Model):
    name = models.CharField(max_length=100000,default='')
    caption = models.CharField(max_length=100000,default='')
    food =  models.ManyToManyField(food)
class Menu(models.Model):
    menu = models.ManyToManyField(category)
class table(models.Model):
    #menu = models.ManyToManyField(food)
    name = models.CharField(max_length=100000,default='')
    #order =  models.ManyToManyField(food)
    #restaurant =  models.ForeignKey('restaurant',on_delete=models.CASCADE)
    menu = models.ManyToManyField(Menu)
    slug = models.SlugField(null=True , unique=True) # new
        
    '''
    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})
    '''
class restaurant(models.Model):
    #menu = models.ManyToManyField(food)
    username =  models.ForeignKey(User, on_delete=models.CASCADE, default='')
    location = models.CharField(max_length=100,default='')
    city = models.CharField(max_length=100,default='')
    orders = models.ManyToManyField('order2')
    menu = models.ManyToManyField(Menu)
    #ownert = models.ForeignKey('auth.User', on_delete=models.CASCADE, default='')
    
class order(models.Model):
    #name = models.CharField(max_length=100,default='')
    #table = models.ForeignKey(table,on_delete=models.CASCADE)
    food =  models.CharField(max_length=100,default='')
class order2(models.Model):
    #name = models.CharField(max_length=100,default='')
    table = models.CharField(max_length=100,default='')
    owner = models.CharField(max_length=10000,default='')
    food =  models.CharField(max_length=10000,default='')
    restaurantx  =  models.CharField(max_length=100,default='')
    time = models.CharField(max_length=100,default='')
    totalprice = models.CharField(max_length=100,default='')
    ordertype = models.CharField(max_length=100,default='')
class Vcart(models.Model):
    #name = models.CharField(max_length=100,default='')
    count = models.CharField(max_length=100,default='1')
    food =  models.CharField(max_length=10000,default='1')
