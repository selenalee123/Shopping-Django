from decimal import Decimal
from rest_framework import serializers
from store.models import Collection, Product

class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)


class ProductSeralizer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    # if name is price <> unit_price in source, remember the source='unit_price'
    price = serializers.DecimalField(max_digits=6, decimal_places=2, source='unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    #collection = serializers.StringRelatedField() another method
    #collection= CollectionSerializer()
    collection= serializers.HyperlinkedRelatedField(
        queryset = Collection.objects.all(),
        view_name='collection-detail'
    )

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
