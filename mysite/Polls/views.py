from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    name = request.GET.get('name')
    return render(request, 'mysite/abouttt.html', {'name: name'})





