from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Count
from budget.models import Budget
from transaction_expense.models import Transaction_Expense
from django.views.generic.edit import CreateView
from budget.views import budget_pie_chart_data


def dashboard_pie_chart(request):
    data = {}

    queryset = Budget.objects.filter(user=request.user).values(
        "name", "category", "amount"
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

    budget_data = budget_pie_chart_data(request)

    transaction_queryset = Transaction_Expense.objects.filter(
        user=request.user
    ).order_by("-date")[:5]
    print("transaction_queryset: ", transaction_queryset)

    return render(
        request,
        "dashboard.html",
        {
            "labels": return_labels,
            "data": return_data,
            "total_budget": budget_data["total_budget"],
            "transactions": budget_data["transactions"],
            "year": budget_data["year"],
            "month": budget_data["month"],
            "transaction_queryset": transaction_queryset,
        },
    )
