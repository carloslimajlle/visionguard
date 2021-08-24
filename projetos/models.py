from django.db import models

# Create your models here.
class Projetos(models.Model):
    id = models.AutoField(primary_key=True)
    nm_projeto = models.CharField(max_length=255)
    dt_inicio = models.DateTimeField(editable=False)
    dt_fim = models.DateTimeField(editable=True)

    class Meta:
        db_table = "projetos"