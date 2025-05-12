from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('nominaciones/', views.crear_nominacion, name='nominacionesList'),
    path('nominacionCreate/', csrf_exempt(views.ver_nominaciones), name='nominacionCreate'),
]