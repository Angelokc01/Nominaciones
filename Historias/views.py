from django.shortcuts import render
from .forms import HistoriasForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .logic.logic_Historias import create_historia, get_Historias
from django.contrib.auth.decorators import login_required
from historiasClinicas.auth0backend import getRole

@login_required
def Historias_list(request):
    role = getRole(request)
    if role == "Medico":
        Historias = get_Historias()
        context = {
          'Historias_list': Historias
        }
        return render(request, 'Measurement/Historias.html', context)
    else:
        return HttpResponse("Paciente no autorizado para ver historias medicas")

    

@login_required
def Historias_create(request):
    role = getRole(request)
    if role == "Medico":
        if request.method == 'POST':
            form = HistoriasForm(request.POST)
            if form.is_valid():
                create_historia(form)
                messages.add_message(request, messages.SUCCESS, 'Historias create successful')
                return HttpResponseRedirect(reverse('historiasList'))
            else:
                print(form.errors)
        else:
            form = HistoriasForm()

        context = {
            'form': form,
        }

        return render(request, 'Measurement/historiaCreate.html', context)
    else:
        return HttpResponse("Paciente no autorizado para crear historias medicas")
    