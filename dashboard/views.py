from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Count
from budget.models import Budget
from transaction_expense.models import Transaction_Expense
from django.views.generic.edit import CreateView
from budget.views import budget_pie_chart_data_dash
import datetime
from calendar import monthrange

"""
This view is used for the dashboard.
"""
def dashboard_pie_chart(request):
    """
    | The following sources has been used:
    | https://docs.djangoproject.com/en/3.0/ref/models/querysets/#month
    | https://stackoverflow.com/questions/4938429/how-do-we-determine-the-number-of-days-for-a-given-month-in-python
    | This function is used to fill the pie chart.
    | It only shows the transactions of the current month and sorts dem descending by date.
    :rtype: returned will be the request, template and data which is used for the template.
    """
    budget_data = budget_pie_chart_data_dash(request)

    today = datetime.date.today()
    transaction_queryset = Transaction_Expense.objects.filter(
        user=request.user, date__iso_year=today.year, date__month=today.month
    ).order_by("-date")

    this_month_in_days = monthrange(today.year, today.month)

    data = {}
    for item in transaction_queryset:
        if item.date.day not in data:
            data[item.date.day] = item.amount
        else:
            data[item.date.day] += item.amount

    transaction_days_label = []
    transaction_days_data = []

    for day in range(1, this_month_in_days[1] + 1):
        if day in data:
            transaction_days_label.append(day)
            transaction_days_data.append(str(data[day]))
        else:
            transaction_days_label.append(day)
            transaction_days_data.append(str(0))

    return render(
        request,
        "dashboard.html",
        {
            "labels": transaction_days_label,
            "data": transaction_days_data,
            "total_budget": budget_data["total_budget"],
            "transactions": budget_data["transactions"],
            "year": budget_data["year"],
            "month": budget_data["month"],
            "transaction_queryset": transaction_queryset,
        },
    )
