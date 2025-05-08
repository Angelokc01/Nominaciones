from django import forms
from .models import Historias

class HistoriasForm(forms.ModelForm):
    class Meta:
        model = Historias
        fields = [
            'value',
            'unit',
            'place',
            #'dateTime',
        ]

        labels = {
            'value' : 'Value',
            'unit' : 'Unit',
            'place' : 'Place',
            #'dateTime' : 'Date Time',
        }
