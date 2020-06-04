from django.http import Http404
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from category.models import Category


# https://docs.djangoproject.com/en/3.0/ref/class-based-views/generic-editing/
class CategoryCreateView(CreateView):
    """
    | CategoryCreateView is used for creating new category by using the generic view for creation.
    | model: is the Model which will be used.
    | success_url: if the input was successful the user will be redirected to the category overview page.
    | template_name: is the templates which will be used for the user input. The budget_add.html is used.
    | https://docs.djangoproject.com/en/3.0/ref/class-based-views/generic-editing/
    """
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
    """
    | The following sources has been used:
    | https://stackoverflow.com/questions/5531258/example-of-django-class-based-deleteview
    | https://stackoverflow.com/questions/17475324/django-deleteview-without-confirmation-template
    | CategoryDeleteView is used to delete categories.
    | model: is the Model which will be used.
    | success_url: if the input was successful the user will be redirected back to list of budgets.
    """
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
