from . import views
from django.urls import path
from django.conf.urls import  url

app_name = 'projetos'

urlpatterns = [
    path('', views.index, name="index"),
    path('<str:projeto_id>/atividades/', views.projeto_atividades, name='projeto_atividades'),
    path('<str:projeto_id>/atividades/add/', views.create_atividade, name='add_atividade'),
    path('add/', views.create, name="add"),
    url(r'^remove/(?P<id>\d+)/$', views.remove, name='remove'),
]