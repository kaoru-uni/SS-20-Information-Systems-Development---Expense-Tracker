from django.shortcuts import render
from django.views.generic import ListView

from dashboard.models import Category
from django.views.generic.edit import CreateView


# Create your views here.


def dashboard_pie_chart(request):
    labels = []
    data = []

    queryset = Category.objects.filter(user=request.user).values('name').annotate(budget_sum=Sum('amount')).order_by(
        '-amount')
    for category in queryset:
        labels.append(category['name'])
        data.append(category['amount'])

    return render(request, 'pie_chart.html', {
        'labels': labels,
        'data': data,
    })


class DashboardCreateView(CreateView):
    model = Category
    fields = ("name", "amount")
    success_url = "/dashboard"
    template_name = "pie_chart1.html"

    class DashboardListView(ListView):
        model = Category
        template_name = "pie_chart1.html"

        def get_queryset(self):
            return Category.objects.filter(user=self.request.user)
