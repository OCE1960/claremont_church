from django.contrib import admin
from django.contrib.auth.models import Group
from django_summernote.admin import SummernoteModelAdmin

from cms.forms.category_form import CategoryAdmin
from cms.forms.role_form import RoleAdmin
from cms.forms.user_form import UserAdmin
from cms.forms.post_form import PostAdmin
from cms.models.category import Category
from cms.models.user import User
from cms.models.post import Post
from cms.models.role import Role

class CmsAdminSite(admin.AdminSite):
    site_header = "Claremont Church CMS Admin"

cms_admin_site = CmsAdminSite(name="admin")
# Now register the new UserAdmin...
cms_admin_site.register(User, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
# cms_admin_site.unregister(Group)
cms_admin_site.register(Category, CategoryAdmin)
cms_admin_site.register(Post, PostAdmin)
cms_admin_site.register(Role, RoleAdmin)
