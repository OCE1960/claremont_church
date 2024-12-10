from django.urls import path

from .views import public_site
from .views import post

app_name = "cms"
urlpatterns = [
    path('', public_site.index, name='index'),
    # path('posts/<int:pk>/', post.index, name='post-detail'),
    path('posts/<int:pk>/', post.PostDetailView.as_view(), name='post-detail'),
]