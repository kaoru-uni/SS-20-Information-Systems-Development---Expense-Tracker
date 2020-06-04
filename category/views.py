from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import View, ListView
from category.models import Category


#https://docs.djangoproject.com/en/3.0/ref/class-based-views/generic-editing/
class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']
    success_url = "/category"
    template_name = "category/category_add.html"
    def form_valid(self, form):
        form_to_save = form.save(commit=False)
        form_to_save.user = self.request.user
        return super(CategoryCreateView, self).form_valid(form)


class CategoryListView(ListView):
    model = Category
    template_name = "category/category.html"

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user).order_by('name')

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = "/category"

    def get_queryset(self):
        logged_in_user = self.request.user
        return self.model.objects.filter(user=logged_in_user)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


# https://stackoverflow.com/questions/25324948/django-generic-updateview-how-to-check-credential
class CategoryEditView(UpdateView):
    model = Category
    fields = ("name",)
    success_url = "/category"
    template_name = "category/category_add.html"

    def get_object(self, *args, **kwargs):
        category_found = super(CategoryEditView, self).get_object(
            *args, **kwargs
        )
        if not category_found.user == self.request.user:
            raise Http404
        return category_found