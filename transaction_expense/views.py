from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Transaction_Expense

from django.shortcuts import Http404


class TransactionExpenseListView(ListView):
    model = Transaction_Expense
    template_name = "transactions.html"

    def get_queryset(self):
        return Transaction_Expense.objects.filter(user=self.request.user)


# https://stackoverflow.com/questions/10382838/how-to-set-foreignkey-in-createview
class TransactionExpenseCreateView(CreateView):
    model = Transaction_Expense
    fields = ("amount", "family", "category")
    success_url = "/transaction/add"
    template_name = "add_transaction.html"

    def form_valid(self, form):
        form_to_save = form.save(commit=False)
        form_to_save.user = self.request.user
        return super(TransactionExpenseCreateView, self).form_valid(form)


# https://stackoverflow.com/questions/25324948/django-generic-updateview-how-to-check-credential
class TransactionExpenseEditView(UpdateView):
    model = Transaction_Expense
    fields = ("amount", "family", "category")
    success_url = "/transaction"
    template_name = "add_transaction.html"

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
