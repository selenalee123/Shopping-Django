from decimal import Decimal
from rest_framework import serializers
from store.models import Collection, Product

#create serializer from model 
#class CollectionSerializer(serializers.Serializer):
class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id','title','products_count']

    products_count = serializers.IntegerField()
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)

#class ProductSeralizer(serializers.Serializer):
class ProductSeralizer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id','title','slug', 'inventory', 'description','unit_price', 'price_with_tax','collection']

    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # # if name is price <> unit_price in source, remember the source='unit_price'
    #price = serializers.DecimalField(max_digits=6, decimal_places=2, source='unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    # #collection = serializers.StringRelatedField() another method
    # #collection= CollectionSerializer()
    # collection= serializers.HyperlinkedRelatedField(
    #     queryset = Collection.objects.all(),
    #     view_name='collection-detail'
    # )

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)

    # def validate(self,data):
    #     if data['password'] !=data['confirm_password']:
    #         return serializers.ValidationError('Passwords do not match')
    #     return data


    def create(self, validated_data):
        product = Product(**validated_data)
        product.other =1 
        product.save()
        return product
    
    
    def update(self, instance, validated_data):
        instance.unit_price = validated_data.get('unit_price', instance.unit_price)
        instance.save()
        return instance

    