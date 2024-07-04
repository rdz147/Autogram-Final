from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext, gettext_lazy as _

class CustomUserCreationForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'birth_date')

class CustomUserChangeForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'birth_date')

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    error_messages = {
        'invalid_login': _(
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': _("This account is inactive."),
    }
