from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('nominaciones/', views.ver_nominaciones, name='nominacionesList'),
    path('nominacionCreate/', views.crear_nominacion, name='nominacionCreate'),
]