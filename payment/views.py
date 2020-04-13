from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .forms import PaymentForm

class Payment(View):
    def get(self, httprequest):
        return HttpResponse("<h1> Your payments are: </h1>")



def AmountInsert(httprequest):
    allPayment = PaymentForm
    context = {
        "form" : allPayment
    }

    return render(httprequest, "allPayment.html", context)