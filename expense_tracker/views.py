from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse("hello world")


def home(request):
    return render(request, 'register/login.html')
