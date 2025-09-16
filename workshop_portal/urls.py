"""
workshop_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""

from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.contrib import admin
from workshop_portal import views
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('workshop/', include('workshop_app.urls')),
    path('reset/', include('django.contrib.auth.urls')),
    path('page/', include('cms.urls')),
    path('statistics/', include('statistics_app.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
