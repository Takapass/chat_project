from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import ChatRoom, UserProfile
from .forms import UserRegistrationForm, UserProfileForm
import random

def home(request):
    return render(request, 'chat/room_list.html')

def chat_room(request, room_name):
    return render(request, 'chat/room.html', {'room_name': room_name})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'auth/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'auth/login.html')

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'profile/profile.html', {'profile': user_profile})

@login_required
def edit_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'profile/edit_profile.html', {'form': form})

def assign_users_to_rooms():
    users = list(UserProfile.objects.all())
    rooms = list(ChatRoom.objects.all())
    for room in rooms:
        assigned_users = random.sample(users, min(len(users), room.capacity))
        room.users.set(assigned_users)