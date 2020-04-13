"""expense_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
<<<<<<< HEAD
from payment.views import PaymentConfigView
from payment.views import amount_insert
=======
from payment.views import Payment, AmountInsert
from . import views
>>>>>>> 580d0b8822608b66c4fb6e68dbabb8e4a4b86ff4

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('paymentview/', PaymentConfigView.as_view()),
    path('all_payment/', amount_insert)
]
