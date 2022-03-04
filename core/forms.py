from cloudinary.models import CloudinaryField
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth.forms import AuthenticationForm


class RegisterForm(UserCreationForm):

    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "phone_number", "password1", "password2"]


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50)
    password = forms.PasswordInput()


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "phone_number", "profile_picture"]


# class ProfileUpdateForm(forms.ModelForm):
#     description = forms.CharField(max_length=500)
#     phone_number = forms.CharField(max_length=15)
#     profile_picture = CloudinaryField("image")
#
#     class Meta:
#         model = Profile
#         fields = ["phone_number", "description", "profile_picture"]
