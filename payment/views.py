from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Payment
from django import forms
from django.shortcuts import Http404


class PaymentListView(ListView):
    model = Payment
    template_name = "payment.html"

    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)


class DateInput(forms.DateInput):
    input_type = "date"


# https://stackoverflow.com/questions/27321692/override-a-django-generic-class-based-view-widget
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ("type", "description", "date")
        widgets = {"date": DateInput()}


class PaymentCreateView(CreateView):
    form_class = PaymentForm
    model = Payment
    success_url = "/payment/add"
    template_name = "add_payment.html"

    def form_valid(self, form):
        form_to_save = form.save(commit=False)
        form_to_save.user = self.request.user
        return super(PaymentCreateView, self).form_valid(form)


# https://stackoverflow.com/questions/25324948/django-generic-updateview-how-to-check-credential
class PaymentEditView(UpdateView):
    form_class = PaymentForm
    model = Payment
    success_url = "/payment"
    template_name = "add_payment.html"

    def get_object(self, *args, **kwargs):
        expense_found = super(PaymentEditView, self).get_object(*args, **kwargs)
        if not expense_found.user == self.request.user:
            raise Http404
        return expense_found


# https://stackoverflow.com/questions/5531258/example-of-django-class-based-deleteview
# https://stackoverflow.com/questions/17475324/django-deleteview-without-confirmation-template
class PaymentDeleteView(DeleteView):
    model = Payment
    success_url = "/payment"

    def get_queryset(self):
        logged_in_user = self.request.user
        return self.model.objects.filter(user=logged_in_user)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
