from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def admin_dashboard(request):
    return render(request, 'index.html')


def ecommerce(request):
    return render(request, 'ecommerce.html')


def analytics(request):
    return render(request, 'analytics.html')


# APP
def chat(request):
    return render(request, 'chat.html')


def contacts(request):
    return render(request, 'contacts.html')


def team(request):
    return render(request, 'team.html')


def calendar(request):
    return render(request, 'calendar.html')


# COMPONENTS
def alert(request):
    return render(request, 'alert.html')


def badge(request):
    return render(request, 'badge.html')


def breadcrumb(request):
    return render(request, 'breadcrumb.html')


def buttons(requests):
    return render(requests, 'buttons.html')


def cards(requests):
    return render(requests, 'cards.html')


def carousel(requests):
    return render(requests, 'carousel.html')


# ICONS

def material_icon(requests):
    return render(requests, 'material-icon.html')


def flag_icon(requests):
    return render(requests, 'flag-icon.html')


# FORMS

def basic_input(requests):
    return render(requests, 'basic-input.html')


def input_group(requests):
    return render(requests, 'input-group.html')


def checbox_radio(requests):
    return render(requests, 'checkbox-radio.html')
