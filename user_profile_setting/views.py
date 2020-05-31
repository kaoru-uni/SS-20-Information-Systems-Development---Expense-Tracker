from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from django.views.generic import TemplateView


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
