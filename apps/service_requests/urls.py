from django.urls import path
from . import views

urlpatterns = [
      path('', views.home, name='home'),
    path('create/', views.create_request, name='create_request'),
    path('list/', views.list_requests, name='list_requests'),
    path('<int:pk>/', views.request_detail, name='request_detail'),
]
