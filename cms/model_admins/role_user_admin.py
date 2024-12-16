from django import forms
from django.contrib import admin

from ..models import Role
from ..models import RoleUser 


class RoleUserCreationForm(forms.ModelForm):

    class Meta:
        model = RoleUser
        fields = ["user", "role"]
        exclude = ["created_at", "updated_at"]
        
        
class RoleUserChangeForm(forms.ModelForm):

    class Meta:
        model = RoleUser
        fields = ["user", "role"]
        exclude = ["created_at", "updated_at"]
        
        
# class RoleUserAdmin(admin.ModelAdmin):
#     # The forms to add and change user instances
#     form = RoleUserChangeForm
#     add_form = RoleUserCreationForm
#     # fields = ["pub_date", "question_text"]
#     fieldsets = [
#         (None, {"fields": ["user", "role"]}),
#         ("Date information", {"fields": ['updated_at']}),
#     ]
#     # inlines = [ChoiceInline]
#     list_display = ["user", "role", "created_at", 'updated_at']
#     list_filter = ["created_at"]
#     search_fields = ["user", "role"]
    

class RoleUserInline(admin.StackedInline):
    model = RoleUser 
    extra = 1
    fields = ["role", "user"]
