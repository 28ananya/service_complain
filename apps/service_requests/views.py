from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from .forms import ServiceRequestForm


@login_required
def create_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.save()
            return redirect('list_requests')
    else:
        form = ServiceRequestForm()
    return render(request, 'service_requests/request_form.html', {'form': form})

@login_required
def list_requests(request):
    requests = ServiceRequest.objects.filter(user=request.user)
    return render(request, 'service_requests/request_list.html', {'requests': requests})

@login_required
def request_detail(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk, user=request.user)
    return render(request, 'service_requests/request_detail.html', {'service_request': service_request})


def home(request):
    return render(request, 'service_requests/home.html')
