"""
URL configuration for claremont_church project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from debug_toolbar.toolbar import debug_toolbar_urls
from django.urls import include, path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

from cms.views.api.users import  router
from cms.admin import cms_admin_site

if not settings.TESTING:
    urlpatterns = [
        path('cms/', include('cms.urls')),
        path('admin/', cms_admin_site.urls),
        path('rest/', include(router.urls)),
        path('api-auth/', include('rest_framework.urls')),
        path('', RedirectView.as_view(url='cms/', permanent=True)),
        path('summernote/', include('django_summernote.urls')),
    ]
    
    urlpatterns += debug_toolbar_urls()
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
