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
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('workshop/', include('workshop_app.urls')),
     # 🔑 Fix here: tell Django to use your existing login.html
    path(
        'reset/login/',
        auth_views.LoginView.as_view(template_name="workshop_app/login.html"),
        name="login"
    ),
    path(
        'reset/logout/',
        auth_views.LogoutView.as_view(template_name="workshop_app/logout.html"),
        name="logout"
    ),

    
    path('reset/', include('django.contrib.auth.urls')),
    path('page/', include('cms.urls')),
    path('statistics/', include('statistics_app.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
