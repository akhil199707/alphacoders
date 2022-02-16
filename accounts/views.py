from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm

# Create your views here.
from django.urls import reverse

from accounts.forms import CustomUserCreationForm


def register_view(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully registered')
            return redirect('login')
    return render(request, 'account/register.html', {'form': form})

#profile
@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def editprofile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, 'details updated')
            return redirect('profilepage')
    else:
        u_form = UserUpdateForm(instance = request.user)
    context = {
        'u_form' : u_form,
    }
    return render(request, 'edit.html', context)
