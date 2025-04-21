from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import api_sign_up, api_log_in


urlpatterns = [
    path('sign-up/', api_sign_up, name='api_sign_up'),
    path('log-in/', api_log_in, name='api_log_in'),
]
