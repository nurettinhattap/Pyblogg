from django.http import HttpResponse
from django.shortcuts import render
from .models import mpost, Product


def index(request):
    mposts = mpost.objects.all()
    return render(request, 'index.html',
                  {'mposts': mposts})


def ab(request):
    products = Product.objects.all()
    return render(request, 'ab.html',
                  {'products': products})


def content(request):
    products = Product.objects.all()
    return render(request, 'content.html',
                  {'products': products})


def new(request):
    return HttpResponse('New Products')

