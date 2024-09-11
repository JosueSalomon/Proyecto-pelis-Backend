from django.urls import path
from .views import *

urlpatterns =[
    path('genero/',GeneroView.as_view(),name='genero'),
    path('genero/<int:id>',GeneroView.as_view(),name='genero_process')
]