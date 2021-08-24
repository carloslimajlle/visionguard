from django.shortcuts import render
from django.conf import settings
from . import urls
from .models import Atividades
from projetos.models import Projetos
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.shortcuts import redirect
from .forms.add_atividade_form import CreateForm


# Create your views here.
@login_required
def index(request):
    projetosList = []

    for projeto in Projetos.objects.all():

        record = {
            'id': projeto.id,
            'nome_projeto': projeto.nm_projeto
        }       

        projetosList.append(record)

    context = {
        'projetosList': projetosList
    }

    return render(request, urls.app_name+'/index.html', context)

@login_required
def remove(request,id):
    atividade = Atividades.objects.get(id=id)
    projeto_id = atividade.projeto.id
    atividade.delete()    
    return redirect('projetos:projeto_atividades',projeto_id)