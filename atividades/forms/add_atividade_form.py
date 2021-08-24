from django import forms
from django.core.exceptions import ValidationError
from atividades.models import Atividades

class CreateForm(forms.Form):

    nome_atividade = forms.CharField(label='Nome atividade', max_length=255)
    data_inicio = forms.DateField(label='Data Início')
    data_fim = forms.DateField(label='Data Fim')
    ind_finalizada = forms.BooleanField(label='Finalizada?')

    def clean_name(self):
        nome_atividade = self.cleaned_data['nome_atividade']
        r = Atividades.objects.filter(nm_atividade=nome_atividade)
        if r.count():
            raise  ValidationError("Atividade já existe!")
        return nome_atividade

    def save(self, commit=True):
        atividade = Atividades.objects.create(
                    nm_projeto=self.cleaned_data['nome_projeto'],
                    dt_inicio=self.cleaned_data['data_inicio'],
                    dt_fim=self.cleaned_data['data_fim'],
                    ind_finalizada=self.cleaned_data['ind_finalizada'],
                )

        return atividade