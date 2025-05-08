from django.shortcuts import render
from .forms import HistoriasForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_Historias import create_historia, get_Historias
from django.contrib.auth.decorators import login_required
from historiasClinicas.auth0backend import getRole

@login_required
def Historias_list(request):
    Historias = get_Historias()
    context = {
        'HistoriasList': Historias
    }
    return render(request, 'historias/Historias.html', context)

def Historias_create(request):
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

    return render(request, 'historias/historiaCreate.html', context)