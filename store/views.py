from django.shortcuts import get_object_or_404
from django.db.models import Count

from .models import Collection, Product
from .serializer import CollectionSerializer, ProductSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view

from store import serializer

# Create your views here.

@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        product_queryset = Product.objects.all()
        serializer = ProductSerializer(product_queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        print(request.data)
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)

@api_view(['GET'])
def product_details(request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(['GET'])
def collection_list(request):
    collections = Collection.objects.annotate(product_count=Count('product')).all()
    serializer = CollectionSerializer(collections, many=True)
    return Response(serializer.data)
