from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm, UsernameField, PasswordChangeForm,PasswordResetForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation

class CustomerRegistrationForm(UserCreationForm):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
   

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        labels = {'email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
                   'email':forms.EmailInput(attrs={'class':'form-control'})
                   }  
 
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=("Old Password"), strip = False , widget = forms.PasswordInput(attrs=
                   {'autocomplete':'current-password','autofocus':True,'class':'form-control'}))
    New_password1 = forms.CharField(label=('New password1'),strip= False, widget = forms.PasswordInput(attrs=
                   {'autocomplete':'New-password', 'autofocus': True,'class':'form-control'}),help_text= password_validation.password_validators_help_text_html)
    New_password2 = forms.CharField(label=("Confirm New password"), strip = False, widget = forms.PasswordInput(attrs={'autocomplete':'new-password','autofocus': True, 'class':'flow-control'}))  


class MyPasswordResetForm(PasswordResetForm):
    Email =  forms.EmailField(label=('Email'),max_length=254, widget = forms.EmailInput(attrs={'autocomplete':'email', 'class':'form-control'}))
