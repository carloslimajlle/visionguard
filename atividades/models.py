from django.db import models
from django.utils.timezone import now
from projetos.models import Projetos

# Create your models here.
class Atividades(models.Model):
    id = models.AutoField(primary_key=True)
    nm_atividade = models.CharField(max_length=255)
    dt_inicio = models.DateTimeField(editable=False)
    dt_fim = models.DateTimeField(editable=True)
    ind_finalizada = models.BooleanField(default=False, blank=True)
    projeto = models.ForeignKey(Projetos, on_delete=models.CASCADE)

    class Meta:
        db_table = "atividades"