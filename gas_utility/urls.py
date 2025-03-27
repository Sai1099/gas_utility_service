# gas_utility/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/', include('customers.urls')),
    path('support/', include('support.urls')),
    path('notifications/', include('notifications.urls')),
]
