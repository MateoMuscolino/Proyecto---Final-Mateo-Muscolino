from django.shortcuts import render, redirect
from .models import Opinion
from django.contrib.auth.decorators import login_required # Importacion que hace obligue al usuario a logearse

def opiniones(request):
    opiniones = Opinion.objects.all().order_by('-fecha')  # Me da todas las opiniones ordenadas por fecha
    return render(request, 'opiniones.html', {'opiniones': opiniones})

@login_required
def agregar_opinion(request):
    if request.method == 'POST':
        libro = request.POST['libro']
        opinion = request.POST['opinion']
        usuario = request.user
        Opinion.objects.create(libro=libro, opinion=opinion, usuario=usuario)
        return redirect('opiniones')  # Redirige a la página de opiniones

    return render(request, 'agregar_opinion.html')

