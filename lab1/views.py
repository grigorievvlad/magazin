from django.shortcuts import render
from django.http import HttpResponse

def first_view(request):
    return render(request, 'first.html')

def index(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contacts(request):
    return render(request, 'contacts.html')


def location(request):
    return render(request, 'location.html')


def catalog(request):
    return render(request, 'catalog.html')


def suppliers(request):
    return render(request, 'suppliers.html')