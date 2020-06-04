from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Transaction_Expense
from category.models import Category
from payment.models import Payment
from django.shortcuts import Http404, render
from django import forms
from datetime import datetime


class DateInput(forms.DateInput):
    """
    DateInput is needed for the forms to have a date picker.
    """
    input_type = "date"


#
class TransactionExpenseForm(forms.ModelForm):
    """
    | The following source has been used:
    | https://stackoverflow.com/questions/27321692/override-a-django-generic-class-based-view-widget
    | The class TransactionExpenseForm is needed to be able to override the normal Django Form
    to have the special widget with a Datepicker option.
    """

    class Meta:
        """
        | According to https://docs.djangoproject.com/en/3.0/topics/db/models/#meta-options
        | and https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        | Meta data can be set to add additional information to a class.
        | model: is the Model which will be used.
        | fields: are the chosen fields which will be shown.
        | widgets: are used to show customized html elements.
        """
        model = Transaction_Expense
        fields = ("date", "amount", "description", "category", "payment")
        widgets = {"date": DateInput()}


class TransactionExpenseListView(ListView):
    """
    | TransactionExpenseListView is used to show all expenses.
    | ListView: is a generic view which offers easier lists with less code to write
    | model: is the Model which will be used.
    | template_name: is the templates where the data will be mapped to.
    """
    model = Transaction_Expense
    template_name = "transactions.html"

    def get_queryset(self):
        """
        get_queryset: is used to define the queryset which will be returned
        :return: filtered data which is owned by the user and ordered by date desc will be returned.
        """
        return Transaction_Expense.objects.filter(user=self.request.user).order_by("-date")


class TransactionExpenseCreateView(CreateView):
    """
    | The following source has been used:
    | https://stackoverflow.com/questions/10382838/how-to-set-foreignkey-in-createview
    | TransactionExpenseCreateView is used for creating new transactions by using the generic view for creation.
    | form_class: is the form which will be used for the user input.
    | model: is the Model which will be used.
    | success_url: if the input was successful the user will be redirected back to the form for further inputs.
    | template_name: is the templates which will be used for the user input.
    """
    form_class = TransactionExpenseForm
    model = Transaction_Expense
    success_url = "/transaction/add"
    template_name = "add_transaction.html"

    def get_form(self, *args, **kwargs):
        """
        | According to https://docs.djangoproject.com/en/3.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.get_form
        | get_form is a mixin which is used to get the current user who is adding a transaction.
        | form.fields["category"]: this query is run before the form is shown that the user can choose from his categories the user has created before.
        | form.fields["payment"]: this query is run before the form is shown that the user can choose from his payment methods the user has created before.
        """
        form = super(TransactionExpenseCreateView, self).get_form(*args, **kwargs)
        form.fields["category"].queryset = Category.objects.filter(
            user=self.request.user
        )
        form.fields["payment"].queryset = Payment.objects.filter(user=self.request.user)
        return form

    def form_valid(self, form):
        """
        form_valid validates and saves the form and redirects to the success url.
        """
        form_to_save = form.save(commit=False)
        form_to_save.user = self.request.user
        return super(TransactionExpenseCreateView, self).form_valid(form)


class TransactionExpenseEditView(UpdateView):
    """
    | The following source has been used:
    | https://stackoverflow.com/questions/25324948/django-generic-updateview-how-to-check-credential
    | form_class: is the form which will be used for the user input.
    | model: is the Model which will be used.
    | success_url: if the input was successful the user will be redirected back to list of transactions.
    | template_name: is the templates which will be used for the user input.
    """
    form_class = TransactionExpenseForm
    model = Transaction_Expense
    success_url = "/transaction"
    template_name = "add_transaction.html"

    def get_form(self, *args, **kwargs):
        """
        | According to https://docs.djangoproject.com/en/3.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.get_form
        | get_form is a mixin which is used to get the current user who is adding a transaction.

        | form.fields["category"]: this query is run before the form is shown that the user can choose from his categories the user has created before.

        | form.fields["payment"]: this query is run before the form is shown that the user can choose from his payment methods the user has created before.
        """
        form = super(TransactionExpenseEditView, self).get_form(*args, **kwargs)
        form.fields["category"].queryset = Category.objects.filter(
            user=self.request.user
        )
        form.fields["payment"].queryset = Payment.objects.filter(user=self.request.user)
        return form

    def get_object(self, *args, **kwargs):
        """
        | According to: https://docs.djangoproject.com/en/3.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.get_object
        | get_object: returns the object which is currently being viewed.
        | It's used to validate that the transactions which was requested is really made by the user.
        | If it's not return an error
        """
        expense_found = super(TransactionExpenseEditView, self).get_object(
            *args, **kwargs
        )
        if not expense_found.user == self.request.user:
            raise Http404
        return expense_found



class TransactionExpenseDeleteView(DeleteView):
    """
    | The following sources has been used:
    | https://stackoverflow.com/questions/5531258/example-of-django-class-based-deleteview
    | https://stackoverflow.com/questions/17475324/django-deleteview-without-confirmation-template
    | TransactionExpenseDeleteView is used to delete transactions.
    | model: is the Model which will be used.
    | success_url: if the input was successful the user will be redirected back to list of transactions.
    """
    model = Transaction_Expense
    success_url = "/transaction"

    def get_queryset(self):
        """
        get_queryset: is used to define the queryset which will be returned
        :return: data which is owned by the user will be returned.
        """
        logged_in_user = self.request.user
        return self.model.objects.filter(user=logged_in_user)

    def get(self, request, *args, **kwargs):
        """
        | This function is used to skip a second delete validation page.
        | Post is send to delete the transaction.
        """
        return self.post(request, *args, **kwargs)



def transaction_expense_pie_chart(request):
    """
    | The following sources has been used:
    | https://simpleisbetterthancomplex.com/tutorial/2020/01/19/how-to-use-chart-js-with-django.html
    | https://www.chartjs.org/docs/latest/charts/bar.html
    | https://docs.djangoproject.com/en/3.0/ref/models/querysets/#range
    | This function is used to fill the pie chart.
    | If a user chooses a range the following variables will be used:
    | start_date: start date range
    | end_date: end date range
    | If no date is selected all transactions will be returned. otherwise the transactions will be sorted by date ascending.

    | Because the data which is queried has the wrong data format for the pie chart it has to be formatted and restructured.
    """
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
