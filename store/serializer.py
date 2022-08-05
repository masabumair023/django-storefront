from decimal import Decimal
from rest_framework import serializers

from .models import Collection, Product, Review


class CollectionSerializer(serializers.ModelSerializer):

    product_count = serializers.IntegerField(read_only = True)
    class Meta:
        model = Collection
        fields = ['id', 'title', 'product_count']


class ProductSerializer(serializers.ModelSerializer):

    price_with_tax = serializers.SerializerMethodField('calculate_tax')

    def calculate_tax(self, product):
        return product.unit_price * Decimal(1.1)

    collection = serializers.PrimaryKeyRelatedField(
        queryset = Collection.objects.all()
    )
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price', 'price_with_tax', 'inventory', 'collection']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'description', 'date', 'product']