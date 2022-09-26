from decimal import Decimal
from rest_framework import serializers

from .models import Collection, Order, OrderItem, Product, Review


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


class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'description', 'date', 'product']



class OrderItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'unit_price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = ['id', 'placed_at', 'payment_status', 'customer', 'items']