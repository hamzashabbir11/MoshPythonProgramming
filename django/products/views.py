from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse('Hello World')



def new(request):
    return HttpResponse('New Products :)')



def Twitter(request):
    return HttpResponse('COAS')