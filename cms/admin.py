from django.contrib import admin

from cms.model_admins.category_admin import CategoryAdmin
from cms.model_admins.role_admin import RoleAdmin
from cms.model_admins.user_admin import UserAdmin
from cms.model_admins.post_admin import PostAdmin
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
