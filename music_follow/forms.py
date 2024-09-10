# streaming/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from .models import *

class LiveSessionForm(forms.ModelForm):
    class Meta:
        model = LiveSession
        fields = ['title']

class ReactionForm(forms.ModelForm):
    class Meta:
        model = Reaction
        fields = ['reaction_type']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', "password2", "tel", "role", "status"]

class CustomUserCreationForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ('role',)
        fields = RegistrationForm.Meta.fields

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["user", "profile_picture"]