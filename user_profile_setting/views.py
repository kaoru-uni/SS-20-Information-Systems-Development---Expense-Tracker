from django.shortcuts import render
import csv
from django.http import HttpResponse
from django.views.generic import TemplateView
from transaction_expense.models import Transaction_Expense
from category.models import Category
from budget.models import Budget
from payment.models import Payment
from django.utils.dateparse import parse_datetime
from django.contrib.auth.models import User


# https://www.youtube.com/watch?v=z4lfVsb_7MA - for creating the login
# https://www.youtube.com/watch?v=3aVqWaLjqS4
class UserProfileSettingConfigView(TemplateView):
    """
    | UserProfileSettingConfigView shows the overview of the whole pfoile page.
    | template_name: is the template which is used.
    """
    template_name = "user_profile_detail.html"

    def form_valid(self, form):
        form_to_save = form.save(commit=False)
        form_to_save.user = self.request.user
        return super(UserProfileSettingConfigView, self).form_valid(form)


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
            [item.type, item.description, item.date, ]
        )

    # writer.writerow(Transaction_Expense)
    response["Content-Disposition"] = 'attachment; filename="payment.csv"'

    return response


def get_payment(data):
    splitted_data = data.split(",")
    payment = splitted_data[0].split(" ")[1]
    description = splitted_data[1]
    return payment, description


# https://docs.djangoproject.com/en/3.0/topics/db/queries/#creating-objects
# https://stackoverflow.com/questions/8636760/parsing-a-datetime-string-into-a-django-datetimefield
# https://www.foxinfotech.in/2018/09/python-how-to-skip-first-line-in-csv.html
def transaction_upload(request):
    template = "user_profile_detail.html"
    prompt = {"order": "Date, Amount, User, Payment, Description, Category"}

    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES["file"]

    data_set = csv_file.read().decode("UTF-8")
    user = request.user

    csv_data = csv.reader(data_set.split("\n"), delimiter=",", quotechar='"')
    next(csv_data)
    for column in csv_data:
        if len(column) != 0:
            csv_date = parse_datetime(column[0])
            csv_amount = column[1]
            csv_payment_data = column[3]
            csv_description = column[4]
            csv_category = column[5]
            user = User.objects.get(username=user)
            category = Category.objects.get(name=csv_category, user=user)
            csv_payment_type, csv_payment_description = get_payment(csv_payment_data)
            payment = Payment.objects.get(type=csv_payment_type, user=user)
            transaction = Transaction_Expense(
                date=csv_date,
                amount=csv_amount,
                user=user,
                category=category,
                payment=payment,
                description=csv_description,
            )
            transaction.save()
    context = {}
    return render(request, template, context)
