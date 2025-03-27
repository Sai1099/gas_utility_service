from django.shortcuts import render, redirect, get_object_or_404
from .models import ServiceRequest
from notifications.models import Notification  # Import the Notification model\
from bson import ObjectId

from .forms import ServiceRequestForm 

def support_home(request):
    return render(request, "support/support_home.html")

def submit_request(request):
    if request.method == "POST":
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('support_home')
    else:
        form = ServiceRequestForm()
    return render(request, "support/home.html", {'form': form})

def request_management(request):
    requests = ServiceRequest.objects.all()
    return render(request, "support/request_management.html", {'requests': requests})
def request_details(request, request_id):
    if not ObjectId.is_valid(request_id):  # Ensure it's a valid ObjectId
        return render(request, "support/error.html", {"message": "Invalid Request ID"})

    request_obj = get_object_or_404(ServiceRequest, id=request_id)
    
    return render(request, "support/request_details.html", {"request": request_obj})

def create_service_request(request):
    if request.method == "POST":
        customer_name = request.POST["customer_name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        request_type = request.POST["request_type"]
        description = request.POST["description"]

        service_request = ServiceRequest.objects.create(
            customer_name=customer_name,
            email=email,
            phone=phone,
            request_type=request_type,
            description=description,
            status="Pending",
        )

        # 🔹 Create a notification
        Notification.objects.create(
            title="New Service Request Created",
            message=f"Service request by {customer_name} has been submitted.",
        )

        return redirect("service_request_list")

    return render(request, "support/create_request.html")
