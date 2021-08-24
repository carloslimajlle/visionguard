from django import forms
from django.core.exceptions import ValidationError
from atividades.models import Atividades
from projetos.models import Projetos

class CreateAtividadeForm(forms.Form):

    nome_atividade = forms.CharField(label='Nome atividade', max_length=255)
    data_inicio = forms.DateField(label='Data Início',help_text='Ex: 2021-08-23')
    data_fim = forms.DateField(label='Data Fim',help_text='Ex: 2021-08-23')
    ind_finalizada = forms.BooleanField(label='Finalizada?', required=False)
    #projeto = forms.ModelMultipleChoiceField(queryset=Projetos.objects.all())    

    def __init__(self, projeto, *args, **kwargs):
        self.projeto = projeto       
        super(CreateAtividadeForm, self).__init__(*args, **kwargs) 
    
    def clean_name(self):
        nome_atividade = self.cleaned_data['nome_atividade']
        r = Atividades.objects.filter(nm_atividade=nome_atividade)
        if r.count():
            raise  ValidationError("Atividade já existe!")
        return nome_atividade

    def save(self, commit=True):

        atividade = Atividades.objects.create(
                    nm_atividade=self.cleaned_data['nome_atividade'],
                    dt_inicio=self.cleaned_data['data_inicio'],
                    dt_fim=self.cleaned_data['data_fim'],
                    ind_finalizada=self.cleaned_data['ind_finalizada'],
                    projeto=self.projeto
                )

        return atividade