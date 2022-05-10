from django.shortcuts import render
from django.db.models import Q,F
from store.models import Product

def say_hello(request):
    # queryset = Product.objects.filter(Qinventory__lt=10, unit_price__lt=20 )
    # queryset = Product.objects.filter(Q(inventory__lt=10)| Q(unit_price__lt=20))
    # queryset = Product.objects.filter(inventory=F('collection__id'))
    queryset = Product.objects.order_by('unit_price','-title')


    return render(request, 'hello.html', {'name': 'Mosh', 'products': list(queryset)})
