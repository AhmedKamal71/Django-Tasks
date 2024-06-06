from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, SignUpForm


def user_login(request):
    if request.user.is_authenticated:
        return redirect("BookStore:book-index")

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully logged in.")
                return redirect("BookStore:book-index")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = LoginForm()
        
    return render(request, "accounts/login.html", {"form": form})


def user_logout(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect("user:login")


def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created. You can now log in.")
            return redirect("user:login")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = SignUpForm()
        
    return render(request, "accounts/signup.html", {"form": form})
