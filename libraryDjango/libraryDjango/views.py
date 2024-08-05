from django.shortcuts import render


def homepage(request):
    return render(request, 'index.html')


def library(request):
    return render(request, 'library.html')
