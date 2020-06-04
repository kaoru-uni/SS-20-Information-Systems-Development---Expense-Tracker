from django.contrib import admin

from .models import Category

"""
Register the app in the admin web interface.
"""
admin.site.register(Category)
