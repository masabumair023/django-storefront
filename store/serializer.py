from decimal import Decimal
from rest_framework import serializers

from .models import Collection, Product


class CollectionSerializer(serializers.ModelSerializer):

    product_count = serializers.IntegerField()
    class Meta:
        model = Collection
        fields = ['id', 'title', 'product_count']

class ProductSerializer(serializers.ModelSerializer):

    price_with_tax = serializers.SerializerMethodField('calculate_tax')
    print(price_with_tax)

    def calculate_tax(self, product):
        return product.unit_price * Decimal(1.1)

    collection = CollectionSerializer()
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price', 'price_with_tax', 'collection']


