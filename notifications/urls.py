from django.urls import path
from .views import notifications_list  # ✅ Import the correct function

urlpatterns = [
    path('', notifications_list, name='notifications_list'),
]
