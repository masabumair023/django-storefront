from django.shortcuts import get_object_or_404

from .models import Product
from .serializer import ProductSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        product_queryset = Product.objects.all()
        serializer = ProductSerializer(product_queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(request.data)
        return Response("This is a post request")

@api_view(['GET'])
def product_details(request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)