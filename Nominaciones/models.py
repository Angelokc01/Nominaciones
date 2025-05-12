from django.db import models

class Nominaciones(models.Model):
    tiktok = models.URLField(max_length=500)
    cancion = models.URLField(max_length=500)
    frase = models.TextField()
    foto = models.ImageField(upload_to='nominaciones/')


    def __str__(self):
        return '%s %s' % (self.value, self.unit)