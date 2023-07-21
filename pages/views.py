from django.shortcuts import render

# Create your views here.

def index(request):
    from django.http import HttpResponse
    return HttpResponse('<h1>Hello World</h1>')



