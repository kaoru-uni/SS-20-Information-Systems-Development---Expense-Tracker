from django.shortcuts import render, redirect
from register.forms import RegisterForm

"""
views.py
==============
The view of the register app.
"""


# https://www.youtube.com/watch?v=z4lfVsb_7MA - for creating the registration

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        """
        check if the form has a valid input.
        if the input is valid save the user and redirect back to the index site.
        """
        if form.is_valid():
            form.save()
            return redirect("/")

    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form": form})
