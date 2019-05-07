from django.shortcuts import render , redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserDetailsUpdateForm, ProfilePictureUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) 
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request , f'Account created for {username}! You are now able to Login')
            return redirect('login')
# When Post request comes a UserCreationForm will be instatiated with Post data 
    else:
        form = UserRegisterForm()
    return render(request , 'userAppTemplates/register.html' , {'form' : form})

# This profile views should only be visible to users if they are logged in
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserDetailsUpdateForm(request.POST, instance=request.user)
        p_form = ProfilePictureUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request , f'Your account has been updated')
            return redirect('profile')
    else:
        u_form = UserDetailsUpdateForm(instance=request.user)
        p_form = ProfilePictureUpdateForm(instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'userAppTemplates/profile.html' , context)