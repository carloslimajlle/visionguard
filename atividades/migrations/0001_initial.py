# Generated by Django 2.1.7 on 2021-08-23 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projetos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atividades',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nm_atividade', models.CharField(max_length=255)),
                ('dt_inicio', models.DateTimeField(editable=False)),
                ('dt_fim', models.DateTimeField()),
                ('ind_finalizada', models.BooleanField(default=False)),
                ('projeto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projetos.Projetos')),
            ],
            options={
                'db_table': 'atividades',
            },
        ),
    ]
