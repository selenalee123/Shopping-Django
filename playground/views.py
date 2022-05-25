from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.db.models import Q, F, Value, Func, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.db import transaction, connection

from tags.models import TaggedItem
from store.models import Product, Order, Customer,Collection,OrderItem


def say_hello(request):
    # queryset = Product.objects.filter(Qinventory__lt=10, unit_price__lt=20 )
    # queryset = Product.objects.filter(Q(inventory__lt=10)| Q(unit_price__lt=20))
    # queryset = Product.objects.filter(inventory=F('collection__id'))
    # queryset = Product.objects.order_by('unit_price','-title')
    # queryset = Product.objects.order_by('unit_price')[0]
    # queryset = Product.objects.latest('unit_price')
    # queryset = Product.objects.all()[5:10]
    # queryset = Product.objects.values('id','title','collection__title')
    # queryset = Product.objects.defer('description')
    # queryset = Product.objects.select_related('collection').all()
    # queryset = Product.objects.prefetch_related('promotion').select_related('collection').all()
    # queryset = Order.objects.select_related('customer').order_by("-placed_at")
    # result = Product.objects.aggregate(Count('id'))
    # result = Product.objects.aggregate(
    #     count= Count('id'), min_price =Min('unit_price')
    # )
    # create a is_new
    # queryset = Customer.objects.annotate(is_new=Value(True))
    # queryset = Customer.objects.annotate(is_new=F('id'))
    # queryset = Customer.objects.annotate(is_new=F('id'))

    # queryset = Customer.objects.annotate(full_name = Func(F('first_name'),Value(''),F('last_name'), function='CONCAT'))
    # queryset = Customer.objects.annotate(full_name = Concat('first_name',Value(''),'last_name'))

    # queryset = Customer.objects.annotate(order_count = Count('order'))
    # discounted_price =ExpressionWrapper(F('unit_price')*0.8, output_field=DecimalField())
    # queryset = Product.objects.annotate(discounted_price = discounted_price)

    # return render(request, 'hello.html', {'name': 'Mosh', 'products': list(queryset)})
    # return render(request, 'hello.html', {'name': 'Mosh', 'result': result})

    # way 1
    # content_type = ContentType.objects.get_for_model(Product)
    # queryset = TaggedItem.objects \
    #     .select_related('tag') \
    #     .filter(content_type=content_type, object_id=1)

    #way 2 
    # get a tag for given object from get_tags_for
    # queryset= TaggedItem.object.get_tags_for(Product,1)

    # how to create collection1 
    #collection = Collection()
    #collection.title = 'Video Games'
    #  method 1
    #collection.featured_product = Product(pk=1)
    #  method 2
    # collection.feature_product_id = 1
    #collection.save()
    #collection.id

    # short form
    #Collection.objects.create(title='a',featured_product_id = 1 )
    #collection.id

    #updating 
    # method 1
    # collection = Collection.objects.get(pk=11)
    # collection.featured_product = None
    # collection.save()

    #method 2
    # Collection.objects.filter(pk=11).update(featured_product=None)

    # collection = Collection(pk=11)
    # collection.delete()
    #__gt : greater than 
    # Collection.object.filter(id__gt =5).delete()

    # with transaction.atomic():
    #     order = Order()
    #     order.customer_id = 1
    #     order.save()

    #     item = OrderItem()
    #     item.order = order
    #     item.product_id =1 
    #     item.quantity =1 
    #     item.unit_price =1 
    #     item.save()
    # render(request, 'hello.html', {'name': 'Mosh'})

    queryset = Product.objects.raw('SELECT * FROM store_product')
    queryset

    #1
    # cursor = connection.cursor()
    # cursor.execute('')
    # cursor.close()

    #2
    # with connection.cursor() as cursor:
    #     cursor.execute()

    return render(request, 'hello.html', {'name': 'Mosh', 'products': list(queryset)})

