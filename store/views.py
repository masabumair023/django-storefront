from urllib import response
from django.shortcuts import render
# from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def product_list(request):
    return Response("Ok")

@api_view(['GET'])
def product_details(request, id):
    return Response(id)