from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.db import transaction
from django.contrib.auth.decorators import login_required

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name")

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("age", "nickname")


@transaction.atomic
def update_profile(request):
    # if request.method == "POST":
    #     user_form = UserForm(request.POST, instance=request.user)
    #     user_profile_form = UserProfileForm(request.POST, instance=request.user.userprofile)
    #     if user_form.is_valid() and user_profile_form.is_valid():
    #         user_form.save()
    #         user_profile_form.save()
    #         return redirect("user:profile")
    # else:
    #     user_form = UserForm(instance=request.user)
    #     user_profile_form = UserProfileForm(instance=request.user.userprofile)
    return render(request, "home/profile.html")

