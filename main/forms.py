from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Page


class SignUpForm(UserCreationForm):
    phonenumber = forms.CharField(max_length=100, required=True)
    address = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "phonenumber",
            "address",
        ]


class PageForm(forms.Form):
    class Meta:
        model = Page
        exclude = ["author"]
