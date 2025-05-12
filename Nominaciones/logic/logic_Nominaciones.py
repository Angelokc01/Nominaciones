from ..models import Nominaciones

def get_nominaciones():
    queryset = Nominaciones.objects.all()  # No se ordena por fecha
    return (queryset)


def create_nominacion(form):
    historia = form.save()
    historia.save()
    return ()