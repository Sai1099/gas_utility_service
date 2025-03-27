from django.urls import path
from . import views

urlpatterns = [
    path('', views.support_home, name='support_home'),
    path('submit/', views.submit_request, name='submit_request'),
    path('requests/', views.request_management, name='request_management'),
    path('requests/<str:request_id>/', views.request_details, name='request_details'),
]
