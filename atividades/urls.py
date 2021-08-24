from . import views
from django.urls import path
from django.conf.urls import  url

app_name = 'atividades'

urlpatterns = [
    path('', views.index, name="index"),
    url(r'^remove/(?P<id>\d+)/$', views.remove, name='remove'),
]