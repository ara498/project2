from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def python(request):
    return HttpResponse('python is high leven open source interpreted scripting language')
def sql(request):
    return HttpResponse('sql is structured quary language which stores data in the form of tables')
    