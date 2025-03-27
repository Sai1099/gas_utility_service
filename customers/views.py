# customers/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from .forms import ServiceRequestForm

@login_required
def create_request(request):
    print("Rendering create_request view")  # Debugging
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user_id = request.user.id
            service_request.save()
            return redirect('request_status')
    else:
        form = ServiceRequestForm()
    return render(request, 'customers/create_request.html', {'form': form})

@login_required
def request_status(request):
    print("Fetching service requests for user:", request.user.id)  # Debugging
    requests = ServiceRequest.objects.filter(user_id=request.user.id)
    print("Found requests:", list(requests))  # Debugging
    return render(request, 'customers/request_status.html', {'requests': requests})
