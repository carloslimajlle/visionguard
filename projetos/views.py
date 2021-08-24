from django.shortcuts import render
from django.conf import settings
from . import urls
from .models import Projetos
from atividades.models import Atividades
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.shortcuts import redirect
from .forms.add_projeto_form import CreateForm
from .forms.add_atividade_form import CreateAtividadeForm


# Create your views here.
@login_required
def index(request):

    projetosList = []

    for projeto in Projetos.objects.all():

        totalAtividades = Atividades.objects.filter(projeto_id=projeto.id).count()
        totalCompletado = Atividades.objects.filter(projeto_id=projeto.id,ind_finalizada=True).count()

        percentualCompleto = 0

        try:
            percentualCompleto = (totalCompletado / totalAtividades) * 100
        except:
            percentualCompleto = 0

        atrasado = "Não"    

        if percentualCompleto < 100:
            atrasado = "Sim"    

        record = {
            'id': projeto.id,
            'nome_projeto': projeto.nm_projeto,
            'data_inicio': projeto.dt_inicio,
            'data_fim': projeto.dt_fim,
            'completo': percentualCompleto,
            'atrasado': atrasado
        }       

        projetosList.append(record)

    context = {
        'projetosList': projetosList
    }

    return render(request, urls.app_name+'/index.html', context)

@login_required
def projeto_atividades(request, projeto_id):

    projeto = Projetos.objects.get(id=projeto_id)
    atividades = Atividades.objects.filter(projeto__id=projeto_id)

    context =  {
        'atividadesList': atividades,
        'projetos': projeto
    }

    return render(request, urls.app_name+'/atividades.html', context)

@login_required
def create(request):
    if request.method == 'POST':

        form = CreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('projetos:index')

    else:
        form = CreateForm()

    return render(request, urls.app_name+'/create.html', {'form': form})

@login_required
def create_atividade(request, projeto_id):

    projeto = Projetos.objects.get(id=projeto_id)     

    if request.method == 'POST':

        form = CreateAtividadeForm(projeto, request.POST)

        if form.is_valid():
            form.save()
            return redirect('projetos:projeto_atividades',projeto_id)

    else:
        form = CreateAtividadeForm(projeto)   

    context =  {
        'projetos': projeto,
        'form': form
    }

    return render(request, urls.app_name+'/create_atividade.html', context)

@login_required
def remove(request,id):
    Projetos.objects.filter(id=id).delete()
    return redirect('projetos:index')