from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from category.models import Category


def category_index(request):
    categories = Category.objects.all()
    context = {
        'categories' : categories
    }
    return render(request, 'catergories.html', context)




