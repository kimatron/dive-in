from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def my_blog(request):
    return HttpResponse("Hello, Blog!")