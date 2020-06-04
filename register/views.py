from django.shortcuts import render, redirect

from register.forms import RegisterForm

"""
views.py
==============
The view of the register app.
"""


def register(response):
    """
    | The following source has been used:
    | https://www.youtube.com/watch?v=z4lfVsb_7MA - for creating the registration
    | This function is used for user registration.
    | Check if the form has a valid input and is a POST.
    | If the input is valid save the user and redirect back to the index site.
    | Otherwise redirect to the register form
    """
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form": form})
