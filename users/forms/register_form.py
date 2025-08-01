from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'display_name']

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Nome de usuário'}),
            'email': forms.EmailInput(attrs={'placeholder': 'E-mail'}),
            'display_name': forms.TextInput(attrs={'placeholder': 'Nome de exibição'}),
        }
