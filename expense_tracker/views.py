from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, "home.html")


def dashboard_pie_chart(request):
    return render(request, "pie_chart1.html", {})

def welcome(request):
    return render(request, "welcome.html", {})
