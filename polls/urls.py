from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('perguntas', views.ultimas_perguntas, name='ultimas_perguntas'),
    path('sobre/', views.sobre, name = 'sobre'),
    path('pergunta/<int:question_id>', views.exibe_questao, name = 'exibe_questao')
]