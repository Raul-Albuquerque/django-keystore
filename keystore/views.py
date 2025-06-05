from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def keystore(request):
    return HttpResponse("Hello World")
