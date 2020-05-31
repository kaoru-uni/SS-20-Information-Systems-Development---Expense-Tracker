from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import View, ListView
from category.models import Category

#https://docs.djangoproject.com/en/3.0/ref/class-based-views/generic-editing/
class CategoryCreateView(CreateView):
        model = Category
        fields = ['name']
        success_url = "/category/add"
        template_name = "add.html"
        def form_valid(self, form):
            form_to_save = form.save(commit=False)
            form_to_save.user = self.request.user
            return super(CategoryCreateView, self).form_valid(form)


class CategoryListView(ListView):
    model = Category
    template_name = "category_form.html"

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)




