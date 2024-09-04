# myapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def artistSignup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'artist-sign.html', {'form': form})


def custom_logout(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request, 'music_follow.html')


@login_required
def profile(request):
    user_profile = Profile.objects.get(user=request.user)
    return render(request, 'profile.html', {
        'user': request.user,
        'profile': user_profile
    })

@csrf_exempt
def upload_profile_picture(request):
    if request.method == 'POST':
        profile_picture = request.FILES.get('profile_picture')
        
        if profile_picture:
            user_profilee = Profile(profile_picture=profile_picture)
            user_profilee.save()
            return JsonResponse({'message': 'Image uploaded successfully!'})
        return JsonResponse({'error': 'Missing name or image.'}, status=400)
    
    return render(request, 'upload.html')

    
