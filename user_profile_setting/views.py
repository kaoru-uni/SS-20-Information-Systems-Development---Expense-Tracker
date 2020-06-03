from django.shortcuts import render
import csv
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from django.views.generic import TemplateView
from transaction_expense.models import Transaction_Expense


# Create your views here.


@login_required
def profile(request, *args, **kwargs):
    return render(request, "profile.html")


class UserProfileSettingConfigView(TemplateView):
    template_name = "user_profile_detail.html"

    def form_valid(self, form):
        form_to_save = form.save(commit=False)
        form_to_save.user = self.request.user
        return super(UserProfileSettingConfigView, self).form_valid(form)


def user_details(httprequest, *args, **kwargs):
    user_profile_details = UserProfileForm()
    context = {
        "form": user_profile_details()
    }
    return render(httprequest, "user_profile_detail.html", context)


def export_csv(request):
    if request.GET.get('sort-btn'):
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Date', 'Amount', 'User', 'Payment', 'Description', 'Category', ])
    for Transaction_Expense in Transaction_Expense.objects.all().values_list('date', 'amount', 'user', 'payment',
                                                                             'description', 'category'):
        writer.writerow(Transaction_Expense)
    response['Content-Disposition'] = 'attachment; filename="transaction.csv"'

    return response
