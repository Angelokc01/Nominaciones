from django import forms
from .models import Historias

class HistoriasForm(forms.ModelForm):
    class Meta:
        model = Historias
        fields = [
            'antecedentes',
            'medicamentos',
            'alergias',
            'cirujias',
            'notas'
        ]

        labels = {
            'antecedentes' : 'Antecedentes',
            'medicamentos' : 'Medicamentos',
            'alergias' : 'Alergias',
            'cirujias' : 'Cirujias',
            'notas' : 'Notas'
            
        }
