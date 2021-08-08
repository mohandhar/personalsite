from django.shortcuts import render


def index(request):
    """Home page of the website"""
    context = dict()
    return render(request, 'home/index.html', context)
