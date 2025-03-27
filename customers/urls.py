# customers/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_request, name='create_request'),
    path('status/', views.request_status, name='request_status'),
]