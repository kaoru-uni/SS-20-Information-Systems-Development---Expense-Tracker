from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View



class CategoryView(View):
    def get(self, request ):
        return HttpResponse("<h1> Categories: </h1>")



