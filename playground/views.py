from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from django.core.exceptions import ObjectDoesNotExist

#MANAGING OBJECTS
def say_hello(request):
    query_set = Product.objects.all()
    list(query_set)
    query_set[0:5]
    query_set.filter().filter().order_by()

#RETRIEVING OBJECTS
def hello(request):
    #use try-catch to catch exceptions
    try:
        product = Product.objects.get(pk=1)
    except ObjectDoesNotExist:
        pass
    
    #using first() method to retrieve the firts object. this returns a queryset
    product = Product.objects.filter(pk=1).first()

    #using the exists() method to first check if the requested object exists in the first place
    exists = Product.objects.filter(pk=1).exists()

#APPLYING MULTIPLE FILTERS
def hello1(request):
    #Products: inventory < 10 and price < 20
    product = Product.objects.filter(inventory__lt=10, unit_price__lt=20)
    product1 = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)