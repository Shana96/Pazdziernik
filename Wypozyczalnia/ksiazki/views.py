from django.http import HttpResponse
from django.shortcuts import render


def start(request):
    return render(request, 'index.html')


def hello(request):
    return HttpResponse('Hello, world!')


# def hello_name(request, s):
#     return HttpResponse(f'Hello, {s} world')


def hello_name(request):
    s = request.GET.get('s', '')
    return HttpResponse(f'Hello, {s} world')
