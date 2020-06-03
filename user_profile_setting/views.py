from django.shortcuts import render
import csv, io
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from dashboard.models import Transaction
from .forms import UserProfileForm
from django.views.generic import TemplateView
from transaction_expense.models import Transaction_Expense
from budget.models import Budget
from payment.models import Payment


# Create your views here.

# https://www.youtube.com/watch?v=z4lfVsb_7MA - for creating the login
# https://www.youtube.com/watch?v=3aVqWaLjqS4
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
    context = {"form": user_profile_details()}
    return render(httprequest, "user_profile_detail.html", context)


# https://docs.djangoproject.com/en/3.0/howto/outputting-csv/
# https://studygyaan.com/django/how-to-export-csv-file-with-django
def export_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type="text/csv")

    writer = csv.writer(response)
    writer.writerow(
        ["Date", "Amount", "User", "Payment", "Description", "Category", ]
    )
    querydata = Transaction_Expense.objects.filter(user=request.user)
    for item in querydata:
        writer.writerow(
            [
                item.date,
                item.amount,
                item.user,
                item.payment,
                item.description,
                item.category,
            ]
        )

    # writer.writerow(Transaction_Expense)
    response["Content-Disposition"] = 'attachment; filename="transaction.csv"'

    return response


def export_budget_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type="text/csv")

    writer = csv.writer(response)
    writer.writerow(
        ["Name", "Amount", "Description", "Category", "Date", ]
    )
    querydata = Budget.objects.filter(user=request.user)
    for item in querydata:
        writer.writerow(
            [
                item.name,
                item.amount,
                item.description,
                item.category,
                item.created_date,
            ]
        )

    # writer.writerow(Transaction_Expense)
    response["Content-Disposition"] = 'attachment; filename="budget.csv"'

    return response


def export_payment_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type="text/csv")

    writer = csv.writer(response)
    writer.writerow(
        ["Card type", "Description", "Date", ]
    )
    querydata = Payment.objects.filter(user=request.user)
    for item in querydata:
        writer.writerow(
            [
                item.type,
                item.description,
                item.date,
            ]
        )

    # writer.writerow(Transaction_Expense)
    response["Content-Disposition"] = 'attachment; filename="payment.csv"'

    return response


def transaction_upload(request):
    template = "user_profile_detail.html"
    prompt = {
        'order': 'Date, Amount, User, Payment, Description, Category'
    }

    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Transaction.objects.update_or_create(
            date=column[0],
            amount=column[1],
            user=column[2],
            payment=column[3],
            description=column[4],
            category=column[5]
        )
    context = {}
    return render(request, template, context)
