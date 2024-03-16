from django.urls import path
from . import views


urlpatterns = [
    path('register_vendor/', views.register_vendor, name='register_vendor'),
    path('vendor_dashboard/', views.vendor_dashboard, name='vendor_dashboard'),
]


