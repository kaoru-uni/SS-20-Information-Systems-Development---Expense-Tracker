from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .forms import PaymentForm


class PaymentConfigView(View):
    def get(self, httprequest):
        return HttpResponse("<h1> Your payments are: </h1>")


def amount_insert(httprequest):
    all_payment = PaymentForm
    context = {
        "form": all_payment
    }

    return render(httprequest, "all_payment.html", context)
