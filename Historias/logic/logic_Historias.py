from ..models import Historias

def get_Historias():
    queryset = Historias.objects.all()  # No se ordena por fecha
    return (queryset)


def create_historia(form):
    historia = form.save()
    historia.save()
    return ()