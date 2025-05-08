from ..models import Historias

def get_Historias():
    queryset = Historias.objects.all().order_by('-dateTime')[:10]
    return (queryset)

def create_historia(form):
    historia = form.save()
    historia.save()
    return ()