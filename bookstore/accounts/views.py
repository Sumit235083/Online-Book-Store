from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm


# REGISTER
def register_view(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Account Created Successfully")

            # REDIRECT TO LOGIN PAGE
            return redirect('/accounts/login/')
        else:

            print(form.errors)

            messages.error(request, "Registration Failed")

    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {
        'form': form
    })


# LOGIN
def login_view(request):

    if request.method == "POST":

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(request, user)

            messages.success(request, "Login Successful")

            # REDIRECT TO HOMEPAGE
            return redirect('/')

        else:

            messages.error(request, "Invalid Username or Password")

    return render(request, 'accounts/login.html')


# LOGOUT
def logout_view(request):

    logout(request)

    return redirect('/accounts/login/')


# PROFILE
@login_required
def profile_view(request):

    return render(request, 'accounts/profile.html')