from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('my name is nagendra')
def nagendra(request):
    return HttpResponse("i am from ongole")