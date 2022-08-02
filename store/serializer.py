from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    price_with_tax = serializers.ReadOnlyField(source='calculate_tax')    
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price', 'price_with_tax', 'collection']