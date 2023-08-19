from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_admin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index.html')
        else:
            messages.success(request, "Their was an error while loggin please try again")
            return redirect('sign-in.html')
    else:
        return render(request, 'sign-in.html', {})
