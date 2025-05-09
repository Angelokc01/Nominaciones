from django.db import models

class Historias(models.Model):
    antecedentes = models.TextField()
    medicamentos = models.TextField()
    alergias = models.TextField()
    cirujias = models.TextField()
    notas = models.TextField()

    def __str__(self):
        return '%s %s' % (self.value, self.unit)