from django.urls import path
from .views import *

urlpatterns =[
    path('genero/',GeneroView.as_view(),name='genero'),
    path('genero/<int:id>',GeneroView.as_view(),name='genero_process'),


    path('usuario/',UsuarioView.as_view(),name='usuario'),
    path('usuario/<int:id>',UsuarioView.as_view(),name='usuario_process'),
]