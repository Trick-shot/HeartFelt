from django.urls import path
from . import views

app_name = 'admin_dashboard'

urlpatterns = [
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard')
]
