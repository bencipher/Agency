from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.error(request, f'Username or Password incorrect, returned {user}')
            return redirect('login')
 
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password_one']
        password2 = request.POST['password_two']
        if password1==password2:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
            user.save();
            return redirect('/')
        elif User.objects.filter(username=username).exists():
            messages.info(request, 'username already taken, try another one.')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'email address already taken, try another one.')
            return redirect('register')
        else:
            messages.info(request, 'Password did not match')
            return redirect('register')
    else:
        return render(request, 'register.html')
