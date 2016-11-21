from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def test(request, *args, **kwargs):
    return HttpResponse('test_string')

def pop_test(request, *args, **kwargs):
    return HttpResponse('<h1> This is popular-questions page! </h1>')

def new_test(request, *args, **kwargs):
    return HttpResponse('<h1> This is new-questions page! </h1>')
