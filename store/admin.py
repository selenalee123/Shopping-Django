from audioop import reverse
from turtle import title
from django.db.models.query import QuerySet
from django.contrib import admin, messages
from django.urls import reverse
from django.utils.html import format_html, urlencode
from django.db.models.aggregates import Count

from tags.models import TaggedItem
from . import models
# Register your models here.


class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'

    def lookups(self, request, model_admin):
        return[
            ('<10', 'Low')
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<10':
            return queryset.filter(inventory__lt=10)

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']
    search_fields= ['title']

    @admin.display(ordering='products_count')  # sorting
    def products_count(self, collection):
        # follow the order admin: app , model, page
        url = (reverse('admin:store_product_changelist')
               + '?'
               + urlencode({
                   'collection__id': str(collection.id)
               }))

        return format_html('<a href="{}">{}</a>', url, collection.products_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )



@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['collection']
    # write a in tile accordingly slug will follow 
    prepopulated_fields= {
        'slug' : ['title']
    }
    # clear inventory 
    actions = ['clear_inventory']
    # new field: 'inventory_status','colection_title'
    list_display = ['title', 'unit_price',
                    'inventory_status', 'colection_title']
    list_editable = ['unit_price']
    list_filter = ['collection', 'last_update', InventoryFilter]
    list_per_page = 10
    list_select_related = ['collection']
    search_fields= ['title']

    def colection_title(self, product):
        return product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'

    @admin.action(description='Clear inventory')
    def clear_inventory(self, request, queryset):
        updated_count= queryset.update(inventory=0)
        self.message_user(
            request,
            f'{updated_count} products were successfully updated',
            messages.ERROR
        )


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership', 'orders']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    list_per_page = 10
    search_fields = ['first_name__istartswith', 'last_name__istartswith']

    @admin.display(ordering='orders_count')  # sorting
    def orders(self, customer):
        # follow the order admin: app , model, page
        url = (reverse('admin:store_order_changelist')
               + '?'
               + urlencode({
                   'customer__id': str(customer.id)
               }))

        return format_html('<a href="{}">{} Orders</a>', url, customer.orders_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            orders_count=Count('order')
        )

class OrderItemInline(admin.TabularInline):# or StackInline
    model = models.OrderItem
    autocomplete_fields= ['product'] 
    min_num= 0
    max_num = 10
    extra = 0

@admin.register(models.Order)
class OderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ['id', 'placed_at', 'customer']
    autocomplete_fields= ['customer']
