# Generated by Django 2.1.7 on 2021-08-23 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atividades', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atividades',
            old_name='projeto_id',
            new_name='projeto',
        ),
    ]