from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Count
from budget.models import Budget
from django.views.generic.edit import CreateView


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

    return render(
        request, "pie_chart1.html", {"labels": return_labels, "data": return_data,}
    )
