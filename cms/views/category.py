from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from cms.models import Category
from cms.forms.category_form import CategoryCreationForm

@method_decorator(login_required, name="dispatch")
class CategoryView(View):
    template_name = "cms/category.html"
    form_class = CategoryCreationForm
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect(reverse('cms:category'))

        return render(request, self.template_name, {"form": form})