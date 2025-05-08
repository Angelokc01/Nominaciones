from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('historias/', views.measurement_list, name='historiaList'),
    path('historiacreate/', csrf_exempt(views.measurement_create), name='historiaCreate'),
]