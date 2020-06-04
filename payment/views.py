from django import forms
from django.shortcuts import Http404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Payment


class PaymentListView(ListView):
    """
    | PaymentListView is used to show all payments
    | model: is the Model which will be used.
    | template_name: is the templates where the data will be mapped to.
    """
    model = Payment
    template_name = "payment.html"

    def get_queryset(self):
        """
        get_queryset is used to return a filtered data result.
        :return: return all payments which are created by the user.
        """
        return Payment.objects.filter(user=self.request.user)


class DateInput(forms.DateInput):
    """
    DateInput is needed for the forms to have a date picker.
    """
    input_type = "date"


class PaymentForm(forms.ModelForm):
    """
    | The following source has been used:
    | https://stackoverflow.com/questions/27321692/override-a-django-generic-class-based-view-widget
    | The class PaymentForm is needed to be able to override the normal Django Form to have the special widget with a Datepicker option.
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
        model = Payment
        fields = ("type", "description", "date")
        widgets = {"date": DateInput()}


class PaymentCreateView(CreateView):
    """
    | PaymentCreateView is used for creating new payments.
    | form_class: is the form which will be used for the user input.
    | model: is the Model which will be used.
    | success_url: if the input was successful the user will be redirected back to the form for further inputs.
    | template_name: is the templates which will be used for the user input.
    """
    form_class = PaymentForm
    model = Payment
    success_url = "/payment/add"
    template_name = "add_payment.html"

    def form_valid(self, form):
        form_to_save = form.save(commit=False)
        form_to_save.user = self.request.user
        return super(PaymentCreateView, self).form_valid(form)


class PaymentEditView(UpdateView):
    """
    | The following source has been used:
    | https://stackoverflow.com/questions/25324948/django-generic-updateview-how-to-check-credential
    | PaymentEditView is used to edit the data which was selected.
    | form_class: is the form which will be used for the user input.
    | model: is the Model which will be used.
    | success_url: if the input was successful the user will be redirected back to the form for further inputs.
    | template_name: is the templates which will be used for the user input.
    """
    form_class = PaymentForm
    model = Payment
    success_url = "/payment"
    template_name = "add_payment.html"

    def get_object(self, *args, **kwargs):
        """
        | According to: https://docs.djangoproject.com/en/3.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.get_object
        | get_object: returns the object which is currently being viewed.
        | It's used to validate that the payment which was requested is really made by the user.
        | If it's not return an error
        """
        expense_found = super(PaymentEditView, self).get_object(*args, **kwargs)
        if not expense_found.user == self.request.user:
            raise Http404
        return expense_found


# https://stackoverflow.com/questions/5531258/example-of-django-class-based-deleteview
# https://stackoverflow.com/questions/17475324/django-deleteview-without-confirmation-template
class PaymentDeleteView(DeleteView):
    """
    | PaymentDeleteView is used to delete payment.
    | model: is the Model which will be used.
    | success_url: if the input was successful the user will be redirected back to list of payments.
    """
    model = Payment
    success_url = "/payment"

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
