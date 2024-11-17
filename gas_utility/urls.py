from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
urlpatterns = [
    path('admin/', admin.site.urls),
     path('', lambda request: redirect('home')),  # Redirect `/` to a valid route
    path('accounts/', include('apps.accounts.urls')),  # User accounts URLs
    path('service-requests/', include('apps.service_requests.urls')),  # Service requests URLs
]
