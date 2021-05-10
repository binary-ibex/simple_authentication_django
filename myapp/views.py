from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# login page
def login_page(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST["username"], password=request.POST["password"]
        )
        if user:
            login(request, user)
            return redirect(home_page)
        else:
            return render(request, "login.html", {"error": "Invalid login"})
    else:
        return render(request, "login.html", {"error": ""})


# home page
@login_required(login_url="/login")
def home_page(request):
    return render(request, "home.html", {})


# logout page
@login_required(login_url="/login")
def logout_page(request):
    logout(request)
    return render(request, "logout.html", {})
