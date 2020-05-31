from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from django.views.generic import TemplateView


# Create your views here.


@login_required
def profile(request, *args, **kwargs):
    return render(request, "profile.html")


class UserProfileSettingConfigView(TemplateView):
    template_name = 'user_profile_detail.html'


def user_details(httprequest, *args, **kwargs):
    user_profile_details = UserProfileForm()
    context = {
        "form": user_profile_details()
    }
    return render(httprequest, "user_profile_detail.html", context)
