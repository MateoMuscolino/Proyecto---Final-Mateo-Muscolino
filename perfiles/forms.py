from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Correo Electrónico", max_length=254, help_text="Requerido. Introduce un correo válido.")
    username = forms.CharField(label="Nombre de usuario", max_length=30, required=True, help_text="Requerido. 30 caracteres como máximo.")
    first_name = forms.CharField(label="Nombre", max_length=30, required=True, help_text="Requerido. 30 caracteres como máximo.")
    last_name = forms.CharField(label="Apellido", max_length=30, required=True, help_text="Requerido. 30 caracteres como máximo.")
class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
