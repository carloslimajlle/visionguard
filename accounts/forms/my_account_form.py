from django import forms
from django.core.exceptions import ValidationError
from Accounts.models import Account

class MyAccountForm(forms.Form):

    email = forms.EmailField(label='Email', max_length=100)
    password = forms. CharField(label='Senha', widget=forms.PasswordInput)
    repeat_password = forms. CharField(label='Repita a Senha', widget=forms.PasswordInput)

    def clean_repeat_password(self):
        pw1 = self.cleaned_data.get('password')
        pw2 = self.cleaned_data.get('repeat_password')
        if pw1 and pw2 and pw1 == pw2:
            return pw2
        raise forms.ValidationError("As senhas não são iguais")

    def save(self, commit=True):
        identify = Identify.objects.create(
                    cpf=self.cleaned_data['cpf'],
                )

        return identify