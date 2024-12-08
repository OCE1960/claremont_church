from django.contrib import admin
from django.contrib.auth.models import Group
from django_summernote.admin import SummernoteModelAdmin

from cms.forms.roles_form import RoleAdmin
from cms.forms.user_form import UserAdmin
from cms.forms.post_form import PostAdmin
from cms.models.user import User
from cms.models.post import Post
from cms.models.role import Role

# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
admin.site.register(Post, PostAdmin)
admin.site.register(Role, RoleAdmin)
