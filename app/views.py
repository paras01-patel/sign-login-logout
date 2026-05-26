from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages


# SIGNUP

def sign(req):

    if req.method == "POST":

        username = req.POST.get('username')
        email = req.POST.get('email')
        password1 = req.POST.get('password1')
        password2 = req.POST.get('password2')

        # PASSWORD CHECK

        if password1 != password2:

            messages.error(req, "Password does not match")
            return redirect('sign')

        # USERNAME CHECK

        if User.objects.filter(username=username).exists():

            messages.error(req, "Username already exists")
            return redirect('sign')

        # EMAIL CHECK

        if User.objects.filter(email=email).exists():

            messages.error(req, "Email already exists")
            return redirect('sign')

        # CREATE USER

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        user.save()

        messages.success(req, "Signup Successfully")

        return redirect('login')

    return render(req, 'sign.html')


# LOGIN PAGE

def login(req):
    if req.method=="POST":
    return render(req, "login.html")