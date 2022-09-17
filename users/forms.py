from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as tr
 
class ProfileForm(forms.ModelForm):

    class Meta:
        model = ProfileModel
        exclude = ['user', 'created_at']


class LoginForm(forms.Form):
    phone_number = forms.CharField(widget=forms.TextInput(), label=tr('phone number'))
    password = forms.CharField(widget=forms.PasswordInput(), label=tr('password'))



class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=(
        forms.PasswordInput(attrs={'class': 'form-control'})

    ), required=True)

    def clean_confirm_password(self, *args, **kwargs):

        if self.cleaned_data['confirm_password'] != self.cleaned_data['password']:
            raise ValidationError('Passwords are not the same !')
        return self.cleaned_data

    class Meta:
        model = UserModel
        fields = ['username', 'phone_number', 'password', 'confirm_password']
    