"""
from django.shortcuts import render
from django.utils import timezone
from .models import Budget

def budget_list(request):
    budget = Budget.objects.filter()
    return render(request, 'budget/budget_list.html', {'budget': budget})
"""