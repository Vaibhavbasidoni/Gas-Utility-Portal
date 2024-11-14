from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import ServiceRequest
from .forms import ServiceRequestForm

def request_list(request):
    requests = ServiceRequest.objects.all().order_by('-created_at')
    return render(request, 'customer_service/request_list.html', {'requests': requests})

def create_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save()
            messages.success(request, 'Service request submitted successfully!')
            return redirect('request_detail', pk=service_request.pk)
    else:
        form = ServiceRequestForm()
    return render(request, 'customer_service/request_form.html', {'form': form})

def request_detail(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    return render(request, 'customer_service/request_detail.html', 
                 {'service_request': service_request})

def request_detail(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    comments = service_request.comments.all()  # Get all comments for this request
    return render(request, 'customer_service/request_detail.html', {
        'service_request': service_request,
        'comments': comments
    })