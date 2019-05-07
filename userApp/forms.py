from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# This will inherit the UserCreationForm
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

# Class 'Meta' is used to make the form interact with a model, When we do form.save() it will save all
# the details to User model
    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1']

class UserDetailsUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username' , 'email']

class ProfilePictureUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']