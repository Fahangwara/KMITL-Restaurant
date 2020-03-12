from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def auth_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            error = "Username or Password Incorrect!!"
            context['username'] = username
            context['password'] = password
            context['error'] = error
            return render(request, 'login.html', context)
        pass
    else:
        return render(request, 'login.html', context)

def auth_logout(request):
    logout(request)
    return redirect('index')
        



