import datetime
import decimal

from django.db.models import Sum
from django.http import Http404
from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from budget.models import Budget
from category.models import Category
from transaction_expense.models import Transaction_Expense

"""
https://simpleisbetterthancomplex.com/tutorial/2020/01/19/how-to-use-chart-js-with-django.html
https://stackoverflow.com/questions/47501469/django-filtering-by-user/47502441
https://stackoverflow.com/questions/19138609/django-aggreagtion-sum-return-value-only/37751814
https://docs.djangoproject.com/en/3.0/ref/models/querysets/#month
https://stackoverflow.com/questions/1416830/django-actual-month-in-queryset
budget_pie_chart_data is used to populate the budget.html page.  
@:param data {}
@:param today is the current date
@:param month is the current month from today as a string
@:param year is the current year from today as a string
total_budget sums up all budget of a user. 
budget_left is the difference between the total budget and all transactions of the current month. 
"""


def budget_pie_chart_data(request):
    data = {}
    today = datetime.date.today()
    month = today.strftime("%B")
    year = today.strftime("%Y")
    budget_data_all = Budget.objects.filter(user=request.user).order_by('name')
    total_budget = Budget.objects.filter(user=request.user).aggregate(Sum("amount"))[
        "amount__sum"
    ]
    total_transactions = (
            Transaction_Expense.objects.filter(user=request.user)
            .filter(date__year=today.year, date__month=today.month)
            .aggregate(Sum("amount"))["amount__sum"]
            or 0.00
    )
    if total_budget is not None:
        budget_left = decimal.Decimal(total_budget) - total_transactions
    else:
        budget_left = 0
    queryset = Budget.objects.filter(user=request.user).values(
        "amount", "category_id", "name"
    )
    for budget in queryset:
        name = budget["name"]

        if name not in data:
            data[name] = budget["amount"]
        else:
            data[name] += budget["amount"]
    return_labels = []
    return_data = []
    for key, value in data.items():
        return_labels.append(key)
        return_data.append(value)

    return render(
        request,
        "budget/budget.html",
        {
            "labels": return_labels,
            "data": return_data,
            "total_budget": total_budget,
            "transactions": budget_left,
            "month": month,
            "year": year,
            "budget_data_all": budget_data_all,
        },
    )


def budget_pie_chart_data_dash(request):
    data = {}
    today = datetime.date.today()
    month = today.strftime("%B")
    year = today.strftime("%Y")
    total_budget = Budget.objects.filter(user=request.user).aggregate(Sum("amount"))[
        "amount__sum"
    ]
    total_transactions = (
            Transaction_Expense.objects.filter(user=request.user)
            .filter(date__year=today.year, date__month=today.month)
            .aggregate(Sum("amount"))["amount__sum"]
            or 0.00
    )
    if total_budget is not None:
        budget_left = decimal.Decimal(total_budget) - total_transactions
    else:
        budget_left = 0
    queryset = Budget.objects.filter(user=request.user).values(
        "amount", "category_id", "name"
    )
    for budget in queryset:
        name = budget["name"]
        if name not in data:
            data[name] = budget["amount"]
        else:
            data[name] += budget["amount"]
    return_labels = []
    return_data = []
    for key, value in data.items():
        return_labels.append(key)
        return_data.append(value)
    return {
        "labels": return_labels,
        "data": return_data,
        "total_budget": total_budget,
        "transactions": budget_left,
        "month": month,
        "year": year,
    }

    """
    | BudgetCreateView is used for creating new transactions by using the generic view for creation.
    | form_class: is the form which will be used for the user input.
    | model: is the Model which will be used.
    | success_url: if the input was successful the user will be redirected to the budget overview page. 
    | template_name: is the templates which will be used for the user input. The budget_add.html is used. 
    | https://docs.djangoproject.com/en/3.0/ref/class-based-views/generic-editing/
    """


class BudgetCreateView(CreateView):
    model = Budget
    fields = ("name", "amount", "description", "category")
    success_url = "/budget"
    template_name = "budget/budget_add.html"

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

    """
    | BudgetCreateView is used to show all budgets. 
    | ListView: is a generic view which offers easier lists with less code to write
    | model: is the Model which will be used.
    | template_name: is the templates where the data will be mapped to.
    | https://docs.djangoproject.com/en/3.0/ref/class-based-views/generic-editing/
    """


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
    template_name = "budget/budget_add.html"

    def get_form(self, *args, **kwargs):
        form = super(BudgetEditView, self).get_form(*args, **kwargs)
        form.fields["category"].queryset = Category.objects.filter(
            user=self.request.user
        )
        return form

    def get_object(self, *args, **kwargs):
        budget_found = super(BudgetEditView, self).get_object(*args, **kwargs)
        if not budget_found.user == self.request.user:
            raise Http404
        return budget_found
