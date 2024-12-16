from django import forms
from django.contrib import admin
from django.contrib import messages
from django.contrib.auth import get_permission_codename
from django.utils.translation import ngettext
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

from ..models import Post


class PostCreationForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["title", "content", "status", "attachment"]
        widgets = {
            'content': SummernoteWidget(),
            # 'bar': SummernoteInplaceWidget(),
        }
        
        
class PostChangeForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["title", "content", "status", "attachment"]
        widgets = {
            'content': SummernoteWidget(),
            # 'bar': SummernoteInplaceWidget(),
        }
     
        
class PostAdmin(admin.ModelAdmin):
    # The forms to add and change user instances
    form = PostChangeForm
    add_form = PostCreationForm
    fieldsets = [
        (None, {"fields": ["category", "title", "content", "status", "attachment"]}),
    ]
    list_display = ["title", "status", "attachment", "updated_at", "created_at"]
    list_filter = ["title", "status"]
    search_fields = ["title", "status"]
    actions = ['make_published']
    # date_hierarchy = "created_at"
    
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)
        
    def has_add_permission(self, request):
        return True
    
    def has_view_permission(self, request, obj=None):
        return True
    
    def has_change_permission(self, request, obj=None):
        return True
    
    def has_delete_permission(self, request, obj=None):
        return True
    
    def has_module_permission(self, request):
        return True
    
    def has_publish_permission(self, request):
        """Does the user have the publish permission?"""
        opts = self.opts
        codename = get_permission_codename("publish", opts)
        return request.user.has_perm("%s.%s" % (opts.app_label, codename))
    
    @admin.action(description="Mark selected stories as published", permissions=['change'])
    def make_published(self, request, queryset):
        updated = queryset.update(status="published")
        self.message_user(
            request,
            ngettext(
                "%d story was successfully marked as published.",
                "%d stories were successfully marked as published.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )  
        
    class Media:
        css = {
            "all": ["cms/my_styles.css"],
        }
        # js = ["my_code.js"] 
