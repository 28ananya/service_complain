from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in
            messages.success(request, 'Registration successful! Welcome, {}!'.format(user.username))
            return redirect('login')  # Redirect to the login page
        else:
            # Print form errors for debugging
            print(form.errors)  # This will log the errors to the console
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('/')  # Redirect to home page after logout
