from django.shortcuts import render, redirect, get_object_or_404 # El get_object_or_404 sirve para que si no nos devuelve el objeto esperado nos de un error 404
from .models import Opinion
from django.contrib.auth.decorators import login_required # Importacion que hace obligue al usuario a logearse
from .forms import EditarOpinionForm

def opiniones(request):
    opiniones = Opinion.objects.all().order_by('-fecha')  # Me da todas las opiniones ordenadas por fecha
    return render(request, 'opiniones.html', {'opiniones': opiniones})


@login_required # Garantiza que solo los usuarios logeados permitan su uso
def agregar_opinion(request): # Agrega nuevas opiniones
    if request.method == 'POST':
        libro = request.POST['libro']
        opinion = request.POST['opinion']
        usuario = request.user
        Opinion.objects.create(libro=libro, opinion=opinion, usuario=usuario)
        return redirect('opiniones')  # Redirige a la página de opiniones

    return render(request, 'agregar_opinion.html')

@login_required
def editar_opinion(request, opinion_id):
    opinion = get_object_or_404(Opinion, id=opinion_id, usuario=request.user)

    if request.method == 'POST':
        form = EditarOpinionForm(request.POST, instance=opinion)
        if form.is_valid():
            form.save()
            return redirect('opiniones')

    else:
        form = EditarOpinionForm(instance=opinion)

    return render(request, 'editar_opinion.html', {'form': form, 'opinion': opinion})

@login_required
def eliminar_opinion(request, opinion_id):
    opinion = get_object_or_404(Opinion, id=opinion_id, usuario=request.user)

    if request.method == 'POST':
        opinion.delete()
        return redirect('opiniones')

    return render(request, 'eliminar_opinion.html', {'opinion': opinion})

@login_required
def tus_opiniones(request):
    usuario = request.user
    opiniones_usuario = Opinion.objects.filter(usuario=usuario).order_by('-fecha')
    return render(request, 'tus_opiniones.html', {'opiniones_usuario': opiniones_usuario})

