"""ProAdministrator URL Configuration

The `urlpatterns` list routes URLs to views.
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views

from userextend.forms import (
    AuthenticationNewForm,
    PasswordChangeViewForm,
    PasswordResetConfirmView,
    PasswordResetViewForm
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('home.urls')),
    path('', include('residents.urls')),
    path('', include('management.urls')),
    path('', include('userextend.urls')),

    # Authentication URLs
    path("login/", views.LoginView.as_view(form_class=AuthenticationNewForm), name="login"),
    path("password_change/", views.PasswordChangeView.as_view(form_class=PasswordChangeViewForm), name="password_change"),
    path("password_reset/", views.PasswordResetView.as_view(form_class=PasswordResetViewForm), name="password_reset"),
    path("reset/<uidb64>/<token>/", views.PasswordResetConfirmView.as_view(form_class=PasswordResetConfirmView), name="password_reset_confirm"),
    path('', include('django.contrib.auth.urls')),
]