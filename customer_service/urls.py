from django.urls import path
from . import views

urlpatterns = [
    path('', views.request_list, name='request_list'),
    path('request/new/', views.create_request, name='create_request'),
    path('request/<int:pk>/', views.request_detail, name='request_detail'),
]