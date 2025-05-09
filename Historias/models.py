from django.db import models

class Historias(models.Model):
    antecedentes = models.CharField(max_length=50)
    medicamentos = models.CharField(max_length=50)
    alergias = models.CharField(max_length=50)
    cirujias = models.CharField(max_length=50)
    notas = models.CharField(max_length=50)

    def __str__(self):
        return '%s %s' % (self.value, self.unit)