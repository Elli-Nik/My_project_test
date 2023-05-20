from django.http import HttpResponse
from django.shortcuts import redirect, render


def index(request):
    return render(request, 'index.html', {})


def about(request):
    return HttpResponse("My name is Elizaveta")


def contacts(request):
    return render(request, 'contacts.html', {})


def hobbies(request):
    return HttpResponse("My hobbies")


def gallery(request):
    return HttpResponse("My gallery")


def interests(request):
    return render(request, 'interests.html', {})

