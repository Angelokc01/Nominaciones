from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('historias/', views.Historias_list, name='historiasList'),
    path('historiacreate/', csrf_exempt(views.Historias_create), name='historiaCreate'),
]