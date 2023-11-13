from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, EditarPerfilForm
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def registro(request): #Maneja el registro de nuevos usuarios
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST) # Si la solicitud es tipo POST crea un usuario con los datos ingresados
        if form.is_valid():
            user = form.save()
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']  # Guarda el correo electrónico
            user.save()
            # Iniciar sesión automáticamente después de registrarse
            login(request, user)
            return redirect('mi_pagina')  # Redirige a la página principal
    else:
        form = CustomUserCreationForm()
    return render(request, 'registro.html', {'form': form})


def iniciar_sesion(request): # Maneja el inicio de sesion de los usuarios
    if request.method == 'POST': # Si la solicitud es tipo POST verifica los datos ingresados
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

def mi_pagina(request): # Renderiza mi pagina principal
    return render(request, 'base.html')
def sobre_mi(request): # Renderiza mi pagina sobre_mi
    return render(request, 'sobre_mi.html')

@login_required
def ver_perfil(request): # Muestra los datos del usuario
    usuario = request.user

    if request.method == 'POST':
        usuario.username = request.POST['username']
        usuario.first_name = request.POST['first_name']
        usuario.last_name = request.POST['last_name']
        usuario.email = request.POST['email']
        usuario.save()
        return redirect('ver_perfil')

    return render(request, 'ver_perfil.html', {'usuario': usuario})

@login_required
def editar_perfil(request): # Permite la edicion del usuario
    usuario = request.user

    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('ver_perfil')
    else:
        form = EditarPerfilForm(instance=usuario)

    return render(request, 'editar_perfil.html', {'form': form})


def cerrar_sesion(request): # Cerrar sesion 
    logout(request)
    # Redirige a la página de inicio después del cierre de sesión
    return redirect('mi_pagina')
