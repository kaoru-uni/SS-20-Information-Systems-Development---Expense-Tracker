from django.views.generic import ListView, CreateView
from .models import Transaction_Expense


class TransactionExpenseListView(ListView):
    model = Transaction_Expense
    template_name = "transactions.html"

    def get_queryset(self):
        return Transaction_Expense.objects.filter(user=self.request.user)


# https://stackoverflow.com/questions/10382838/how-to-set-foreignkey-in-createview
class TransactionExpenseCreateView(CreateView):
    model = Transaction_Expense
    fields = ("amount", "family")
    success_url = "/transaction/add"
    template_name = "add_transaction.html"

    def form_valid(self, form):
        form_to_save = form.save(commit=False)
        form_to_save.user = self.request.user
        return super(TransactionExpenseCreateView, self).form_valid(form)
