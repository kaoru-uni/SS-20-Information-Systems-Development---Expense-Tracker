from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Transaction_Expense
from category.models import Category
from payment.models import Payment
from django.shortcuts import Http404, render
from django import forms
from datetime import datetime


class DateInput(forms.DateInput):
    input_type = "date"


# https://stackoverflow.com/questions/27321692/override-a-django-generic-class-based-view-widget
class TransactionExpenseForm(forms.ModelForm):
    class Meta:
        model = Transaction_Expense
        fields = ("date", "amount", "description", "category", "payment")
        widgets = {"date": DateInput()}


class TransactionExpenseListView(ListView):
    model = Transaction_Expense
    template_name = "transactions.html"

    def get_queryset(self):
        return Transaction_Expense.objects.filter(user=self.request.user).order_by("-date")


# https://stackoverflow.com/questions/10382838/how-to-set-foreignkey-in-createview
class TransactionExpenseCreateView(CreateView):
    form_class = TransactionExpenseForm
    model = Transaction_Expense
    success_url = "/transaction/add"
    template_name = "add_transaction.html"

    def get_form(self, *args, **kwargs):
        form = super(TransactionExpenseCreateView, self).get_form(*args, **kwargs)
        form.fields["category"].queryset = Category.objects.filter(
            user=self.request.user
        )
        form.fields["payment"].queryset = Payment.objects.filter(user=self.request.user)
        return form

    def form_valid(self, form):
        form_to_save = form.save(commit=False)
        form_to_save.user = self.request.user
        return super(TransactionExpenseCreateView, self).form_valid(form)


# https://stackoverflow.com/questions/25324948/django-generic-updateview-how-to-check-credential
class TransactionExpenseEditView(UpdateView):
    form_class = TransactionExpenseForm
    model = Transaction_Expense
    success_url = "/transaction"
    template_name = "add_transaction.html"

    def get_form(self, *args, **kwargs):
        form = super(TransactionExpenseEditView, self).get_form(*args, **kwargs)
        form.fields["category"].queryset = Category.objects.filter(
            user=self.request.user
        )
        form.fields["payment"].queryset = Payment.objects.filter(user=self.request.user)
        return form

    def get_object(self, *args, **kwargs):
        expense_found = super(TransactionExpenseEditView, self).get_object(
            *args, **kwargs
        )
        if not expense_found.user == self.request.user:
            raise Http404
        return expense_found


# https://stackoverflow.com/questions/5531258/example-of-django-class-based-deleteview
# https://stackoverflow.com/questions/17475324/django-deleteview-without-confirmation-template
class TransactionExpenseDeleteView(DeleteView):
    model = Transaction_Expense
    success_url = "/transaction"

    def get_queryset(self):
        logged_in_user = self.request.user
        return self.model.objects.filter(user=logged_in_user)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


# https://simpleisbetterthancomplex.com/tutorial/2020/01/19/how-to-use-chart-js-with-django.html
# https://www.chartjs.org/docs/latest/charts/bar.html
# https://docs.djangoproject.com/en/3.0/ref/models/querysets/#range
def transaction_expense_pie_chart(request):
    labels = []
    data = []

    start_date = request.POST.get("start_date")
    end_date = request.POST.get("end_date")

    if start_date is not None and end_date is not None:
        formatted_start_date = datetime.strptime(start_date, "%Y-%m-%d")
        formatted_end_date = datetime.strptime(end_date, "%Y-%m-%d")

        query = (
            Transaction_Expense.objects.filter(user=request.user)
                .filter(date__range=(formatted_start_date, formatted_end_date))
                .order_by("date")
        )
    else:
        query = Transaction_Expense.objects.filter(user=request.user).order_by("date")

    for transaction in query:
        labels.append(f"{transaction.category}, {transaction.date.date()}")
        data.append(str(transaction.amount))

    return render(request, "pie_chart.html", {"labels": labels, "data": data, })
