from django import forms
from django.contrib import admin
from django.template.defaultfilters import slugify

from ..models import Category


class CategoryCreationForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ["key", "status"]
        
        
class CategoryChangeForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ["key", "status"]
        
        
class CategoryAdmin(admin.ModelAdmin):
    # The forms to add and change user instances
    form = CategoryChangeForm
    add_form = CategoryCreationForm
    list_display = ["key", "slug", "status", "created_at", 'updated_at']
    list_filter = ["created_at"]
    search_fields = ["key", "status"]
    
    def save_model(self, request, obj, form, change):
        obj.slug = slugify(form.cleaned_data['key'])
        super().save_model(request, obj, form, change)
    
    class Media:
        css = {
            # "all": ["cms/my_styles.css"],
        }
        # js = ["my_code.js"] 