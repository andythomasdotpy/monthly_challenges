from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def january(request):
    return HttpResponse("Hi, January!")


def february(request):
    return HttpResponse("Hello, February!")

def march(request):
    return HttpResponse("Hi, March")


def monthly_challenge(request):
    return HttpResponse()