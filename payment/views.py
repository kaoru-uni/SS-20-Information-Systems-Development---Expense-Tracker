from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import PaymentForm


class PaymentConfigView(TemplateView):
    template_name = 'all_payment.html'


def amount_insert(httprequest, *args, **kwargs):
    all_payment = PaymentForm()
    context = {
        "form": all_payment
    }
    return render(httprequest, "all_payment.html", context)
