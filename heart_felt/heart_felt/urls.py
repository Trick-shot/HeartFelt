from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('admin_dashboard/', include('admin_dashboard.urls')),
    path('404-page', views.p404, name='404'),
    # path('login-admin/', views.login_admin, name='login'),
    # path('login-admin/', include('django.contrib.auth.urls')),
]
