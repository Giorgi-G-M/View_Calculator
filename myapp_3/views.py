from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def even_odden(request,number):
    if number % 2 == 0:
        result = "even"
    else:
        result = "odd"
    return HttpResponse(f"<h1>This number is {result} </h1>")