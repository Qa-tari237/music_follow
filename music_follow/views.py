from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import Profile
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password, make_password
from .forms import *
from django.contrib.auth.forms import AuthenticationForm

def signup(request):
    if request.method == 'POST':
        request_data = {
            "username": request.POST["username"],
            "email": request.POST["email"],
            "tel": request.POST["tel"],
            "password1": request.POST["password1"],
            "password2": request.POST["password2"]
        }
        form = CustomUserCreationForm(request_data)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, "signup.html", {"errors": form.errors})
    else:
        form = RegistrationForm()
        return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        print(f"User: {form}")
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            if user.role == "admin":
                return render(request, "admin.html")
            elif user.role == "artist":
                return render(request, "artist.html")
            else:
                return render(request, 'music_follow.html')
        else:
            print(form.errors)
            return render(request, 'login.html', {'errors': form.errors})
    else:
        return render(request, "login.html")

def artistSignup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin')
        return render(request, "artist-sign.html", {"errors": form.errors})
    else:
        form = RegistrationForm()
    return render(request, 'artist-sign.html', {'form': form})


def custom_logout(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request, 'music_follow.html')


@login_required
def profile(request):
    if request.method == "GET":
        user_profile = None
        try:
            user_profile = Profile.objects.get(user=request.user)
        except Exception as e:
            pass

        user_info = CustomUser.objects.get(pk=request.user.id)
        user_complete_dict = {}

        if user_profile :
            user_complete_dict = {
                "profile": user_profile.profile_picture,
                "other": user_info
            }
        else :
            user_complete_dict = {
                "profile": None,
                "other": user_info
            }
        return render(request, 'profile.html', {"info": user_complete_dict})
    else:
        pass

@csrf_exempt
def upload_profile_picture(request):
    if request.method == 'POST':
        user = CustomUser.objects.get(username=request.user)
        data = {
            "user": user.pk
        }
        user_profilee = ProfileForm(data, request.FILES)
        if user_profilee.is_valid():
            user_profilee.save()
            return redirect("profile")
        else:
            return render(request, "upload.html", {"errors": user_profilee.errors})
    return render(request, 'upload.html')

    
