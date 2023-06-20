from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('perguntas', views.ultimas_perguntas, name='ultimas_perguntas'),
]