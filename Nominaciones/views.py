from django.shortcuts import render, redirect
from .models import Nominaciones

def crear_nominacion(request):
    if request.method == 'POST':
        tiktok = request.POST.get('tiktok')
        cancion = request.POST.get('cancion')
        frase = request.POST.get('frase')
        foto = request.FILES.get('foto')

        Nominaciones.objects.create(
            tiktok=tiktok,
            cancion=cancion,
            frase=frase,
            foto=foto
        )
        return redirect('nominacionCreate')

    return render(request, 'nominacionCreate.html')

def ver_nominaciones(request):
    nominaciones = Nominaciones.objects.all().order_by('-id')
    return render(request, 'Nominaciones.html', {'nominaciones': nominaciones})
