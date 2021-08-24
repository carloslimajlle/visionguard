from django import forms
from django.core.exceptions import ValidationError
from projetos.models import Projetos

class CreateForm(forms.Form):

    nome_projeto = forms.CharField(label='Nome projeto', max_length=255)
    data_inicio = forms.DateField(label='Data Início')
    data_fim = forms.DateField(label='Data Fim')

    def clean_name(self):
        nome_projeto = self.cleaned_data['nome_projeto']
        r = Projetos.objects.filter(nm_projeto=nome_projeto)
        if r.count():
            raise  ValidationError("Projeto já existe!")
        return nome_projeto

    def save(self, commit=True):
        projeto = Projetos.objects.create(
                    nm_projeto=self.cleaned_data['nome_projeto'],
                    dt_inicio=self.cleaned_data['data_inicio'],
                    dt_fim=self.cleaned_data['data_fim'],
                )

        return projeto