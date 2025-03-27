from django.shortcuts import render
from .models import Notification  # ✅ Import only the model

def notifications_list(request):
    notifications = Notification.objects.all()
    return render(request, "notifications/notifications_list.html", {"notifications": notifications})
