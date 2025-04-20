from django import forms
from .models import Table

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ['name']