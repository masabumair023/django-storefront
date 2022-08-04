from logging import raiseExceptions
from django.shortcuts import get_object_or_404
from django.db.models import Count

from .models import Collection, Product
from .serializer import CollectionSerializer, ProductSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

# Create your views here.

class ProductList(APIView):
    def get(self, request):
        product_queryset = Product.objects.all()
        serializer = ProductSerializer(product_queryset, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)


class ProductDetails(APIView):
    def get(self, request, id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    def delete(self, request, id):
        product = get_object_or_404(Product, pk=id)
        product.delete()
        return Response("Product has been deleted")


class CollectionList(APIView):
    def get(self, request):
        collections = Collection.objects.annotate(product_count=Count('product')).all()
        serializer = CollectionSerializer(collections, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)


class CollectionDetails(APIView):
    def get(self, request, id):
        collection = get_object_or_404(Collection.objects.annotate(product_count=Count('product')), pk=id)
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)
    def delete(self, request, id):
        collection = get_object_or_404(Collection, pk=id)
        collection.delete()
        return Response("The collection has been deleted")
    def put(self, request, id):
        collection = get_object_or_404(Collection, pk=id)
        serializer = CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        collection.title = serializer.validated_data['title']
        collection.save()
        return Response("Collection has been updated")

