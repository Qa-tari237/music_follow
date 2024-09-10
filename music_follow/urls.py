from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('artist_signup/', views.artistSignup, name='artistSignup'),
    path('login/', views.login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('upload/', views.upload_profile_picture, name='upload'),    
    path("custom/admin/", views.artistSignup, name="admin")
]