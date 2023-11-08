from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login,authenticate
from django.contrib import messages

def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            # Iniciar sesión automáticamente después de registrarse
            login(request, user)
            return redirect('mi_pagina')  # Redirigir a la página principal
    else:
        form = CustomUserCreationForm()
    return render(request, 'registro.html', {'form': form})


def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # El inicio de sesión fue exitoso
            messages.success(request, 'Inicio de sesión exitoso')
            return redirect('mi_pagina')
        else:
            # El inicio de sesión falló
            messages.error(request, 'Inicio de sesión fallido. Verifica tus datos.')

    return render(request, 'inicio_sesion.html')

def mi_pagina(request):
    return render(request, 'base.html')
def sobre_mi(request):
    return render(request, 'sobre_mi.html')