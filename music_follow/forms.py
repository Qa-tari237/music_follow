# streaming/forms.py
from django import forms
from .models import LiveSession, Reaction

class LiveSessionForm(forms.ModelForm):
    class Meta:
        model = LiveSession
        fields = ['title']

class ReactionForm(forms.ModelForm):
    class Meta:
        model = Reaction
        fields = ['reaction_type']
        

