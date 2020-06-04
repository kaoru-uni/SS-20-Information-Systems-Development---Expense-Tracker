from django.contrib import admin

from .models import Payment

"""
Register the app in the admin web interface.
"""
admin.site.register(Payment)
