from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from store.models import Product
from django.core.exceptions import ObjectDoesNotExist

#MANAGING OBJECTS
def say_hello1(request):
    query_set = Product.objects.all()
    list(query_set)
    query_set[0:5]
    # query_set.filter().filter().order_by()
    return render(request, 'hello.html', {'products': query_set})
    

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
    pass


#FILTERING DATA
def say_hello2(request):
    query_set = Product.objects.all()
    products = query_set.filter(unit_price__range=(20, 30)) #filter number
    products2 = query_set.filter(title__contains='Coffee') #filter strings
    products3= query_set.filter(title__icontains='coffee') #to make the search non case sensitive use 'icontains'
    products3= query_set.filter(title__istartswith='coffee')
    # products3= query_set.filter(title__iendswith='coffee')
    products3= query_set.filter(last_update__year=2022)
    products3= query_set.filter(description__isnull=True)
    
    return render(request, 'hello.html', {'products': products3}) #filter strings


#COMPLEX FILTERING
def say_hello3(request):
    #Products: inventory < 10 and price < 20
    product = Product.objects.filter(inventory__lt=10, unit_price__lt=20)
    product1 = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)
    products2 = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    # query_set.filter().filter().order_by()
    
    return render(request, 'hello.html', {'products': products2})


#REFERENCING FIELDS USING F OBJECTS
#used to compare two fields in a model
def  say_hello4(request):
    # e.g. Product: inventory=price
    query_set = Product.objects.filter(inventory=F('unit_price'))
    return render(request, 'hello.html', {'products': query_set})



#SORTING DATA
def  say_hello(request):
    query_set = Product.objects.order_by('title')
    return render(request, 'hello.html', {'products': query_set})