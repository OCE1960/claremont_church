from django.urls import path

from .views import public_site

app_name = "cms"
urlpatterns = [
    path('', public_site.index, name='index'),
]