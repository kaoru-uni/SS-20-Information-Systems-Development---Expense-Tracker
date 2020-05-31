from django.http import Http404
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import View, ListView
from budget.models import Budget


#https://docs.djangoproject.com/en/3.0/ref/class-based-views/generic-editing/
class BudgetCreateView(CreateView):
        model = Budget
        fields = ['name', 'amount', 'description']
        success_url = "/budget"
        template_name = "budget_add.html"
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
    fields = ("name", "amount", "description",)
    success_url = "/budget"
    template_name = "budget_add.html"

    def get_object(self, *args, **kwargs):
        budget_found = super(BudgetEditView, self).get_object(
            *args, **kwargs
        )
        if not budget_found.user == self.request.user:
            raise Http404
        return budget_found