from django import forms
from .models import User

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['phone_number', 'name']  # Используем поля модели User
        widgets = {
            'phone_number': forms.TextInput(attrs={'placeholder': '+7(999)999-99-99'}),
        }
