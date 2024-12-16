from django import forms
from django.contrib import admin

from ..models import Role
from .role_user_admin import RoleUserInline 


class RoleCreationForm(forms.ModelForm):

    class Meta:
        model = Role
        fields = ["key", "label", "status"]
        
        
class RoleChangeForm(forms.ModelForm):

    class Meta:
        model = Role
        fields = ["key", "label", "status"]
        
        
class RoleAdmin(admin.ModelAdmin):
    # The forms to add and change user instances
    form = RoleChangeForm
    add_form = RoleCreationForm
    # fields = ["pub_date", "question_text"]
    fieldsets = [
        (None, {"fields": ["key", "label", "status"]}),
        # ("Date information", {"fields": ['updated_at']}),
    ]
    # inlines = [ChoiceInline]
    list_display = ["key", "label", "status", "created_at", 'updated_at']
    list_filter = ["created_at"]
    search_fields = ["key", "label", "status"]
    inlines = [RoleUserInline]
    
    class Media:
        css = {
            # "all": ["cms/my_styles.css"],
        }
        # js = ["my_code.js"] 