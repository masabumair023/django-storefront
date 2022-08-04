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
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)

@api_view(['GET', 'DELETE'])
def product_details(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        product.delete()
        return Response("Product has been deleted")

@api_view(['GET', 'POST'])
def collection_list(request):
    if request.method == 'GET':
        collections = Collection.objects.annotate(product_count=Count('product')).all()
        serializer = CollectionSerializer(collections, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # serializer.save()
        return Response(serializer.validated_data)

@api_view(['GET', 'DELETE', 'PUT'])
def collection_details(request, id):
    collection = get_object_or_404(Collection.objects.annotate(product_count=Count('product')), pk=id)
    if request.method == 'GET':
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        collection.delete()
        return Response("The collection has been deleted")
    elif request.method == 'PUT':
        serializer = CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
