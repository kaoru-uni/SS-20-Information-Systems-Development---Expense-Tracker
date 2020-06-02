from typing import Any, Union

from django.db.models import Sum, Count
from django.http import Http404
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import View, ListView
from budget.models import Budget
from transaction_expense.models import Transaction_Expense
from django.shortcuts import render
from category.models import Category
import datetime
import decimal

"""
https://simpleisbetterthancomplex.com/tutorial/2020/01/19/how-to-use-chart-js-with-django.html
https://stackoverflow.com/questions/47501469/django-filtering-by-user/47502441
https://stackoverflow.com/questions/19138609/django-aggreagtion-sum-return-value-only/37751814
https://docs.djangoproject.com/en/3.0/ref/models/querysets/#month
https://stackoverflow.com/questions/1416830/django-actual-month-in-queryset
total_budget sums up all budget of a user. 
budget_left is the difference between the total budget and all transactions of the current month. 
"""


def budget_pie_chart(request):
    labels = []
    data = []
    today = datetime.date.today()
    month = today.strftime('%B')
    year = today.strftime('%Y')
    total_budget = Budget.objects.filter(user=request.user).aggregate(Sum("amount"))['amount__sum'] or 0.00
    total_transactions = Transaction_Expense.objects.filter(user=request.user).filter(date__year=today.year,date__month=today.month).aggregate(Sum("amount"))['amount__sum'] or 0.00
    budget_left = decimal.Decimal(total_budget) - total_transactions
    query = Budget.objects.filter(user=request.user).values("amount", "category_id").annotate(
        dcount=Count("category_id")).order_by("amount")
    for entry in query:
        labels.append(entry['category_id'])
        data.append(entry['amount'])

    return render(request, 'budget_pie_chart.html', {
        "labels": labels,
        "data": data,
        "total_budget" : total_budget,
        "transactions" : budget_left,
        "month" : month,
        "year" : year,
    })



# https://docs.djangoproject.com/en/3.0/ref/class-based-views/generic-editing/
class BudgetCreateView(CreateView):
    model = Budget
    fields = ("name", "amount", "description", "category")
    success_url = "/budget"
    template_name = "budget_add.html"

    def get_form(self, *args, **kwargs):
        form = super(BudgetCreateView, self).get_form(*args, **kwargs)
        form.fields["category"].queryset = Category.objects.filter(
            user=self.request.user
        )
        return form

    def form_valid(self, form):
        form_to_save = form.save(commit=False)
        form_to_save.user = self.request.user
        return super(BudgetCreateView, self).form_valid(form)



class BudgetListView(ListView):
    model = Budget
    template_name = "budget.html"

    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)


class BudgetDeleteView(DeleteView):
    model = Budget
    success_url = "/budget"

    def get_queryset(self):
        logged_in_user = self.request.user
        return self.model.objects.filter(user=logged_in_user)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


# https://stackoverflow.com/questions/25324948/django-generic-updateview-how-to-check-credential
class BudgetEditView(UpdateView):
    model = Budget
    fields = ("name", "amount", "description", "category")
    success_url = "/budget"
    template_name = "budget_add.html"

    def get_form(self, *args, **kwargs):
        form = super(BudgetEditView, self).get_form(*args, **kwargs)
        form.fields["category"].queryset = Category.objects.filter(
            user=self.request.user
        )
        return form

    def get_object(self, *args, **kwargs):
        budget_found = super(BudgetEditView, self).get_object(
            *args, **kwargs
        )
        if not budget_found.user == self.request.user:
            raise Http404
        return budget_found