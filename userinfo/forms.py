from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.db.models import fields
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = models.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    """def clean(self):
        email = self.cleaned_data('email')
        try:
            if User.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
                raise forms.ValidationError(f'Username "{email}" is already in use.')
            return email
        except:
            pass"""



    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')
        #print(email)
        #match=User.objects.filter(email=email)
        #print("Info",match)
        try:
            match=User.objects.filter(email=email)
            if User.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
                raise forms.ValidationError(f'Email "{email}" is already exist.')
        except User.DoesNotExist:
            return email
        #raise forms.ValidationError('This email address is already Exist.')

        """# Check to see if any users already exist with this email as a username.
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return email

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This email address is already in use.')"""
class UserUpdateForm(forms.ModelForm):
    email= forms.EmailField()
    class Meta:
        model = User
        fields =['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','phone','image']