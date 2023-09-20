from django.urls import path
from . import views

app_name = 'admin_dashboard'

urlpatterns = [
    path('', views.admin_dashboard, name='admin_home'),
    path('ecommerce', views.ecommerce, name='ecommerce'),
    path('analytics', views.analytics, name='analytics'),
    path('chat', views.chat, name='chat'),
    path('contacts', views.contacts, name='contacts'),
    path('team', views.team, name='team'),
    path('calendar', views.calendar, name='calendar'),
    path('alert', views.alert, name='alert'),
    path('badge', views.badge, name='badge'),
    path('breadcrumb', views.breadcrumb, name='breadcrumb'),
    path('cards', views.cards, name='card'),
    path('carousel', views.carousel, name='carousel'),

]
