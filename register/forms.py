from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    """
    | This class is used as an form for the registration.
    | email: creates an email field forms which checks if the email is valid.
    """
    email = forms.EmailField()

    class Meta:
        """
        | According to https://docs.djangoproject.com/en/3.0/topics/db/models/#meta-options
        | and https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        | Meta data can be set to add additional information to a class.
        | model: is the Model which will be used.
        | fields: are the chosen fields which will be shown.
        """
        model = User
        fields = ["username", "email", "password1", "password2"]
