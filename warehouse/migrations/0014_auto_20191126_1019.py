# Generated by Django 2.2.7 on 2019-11-26 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0013_auto_20191126_1010'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fatoaluno',
            old_name='indiceIngressantesRegiaoConcluinteEstadual',
            new_name='indiceConcluintesRegiaoEstadual',
        ),
        migrations.RenameField(
            model_name='fatoaluno',
            old_name='indiceIngressantesRegiaoConcluinteFederal',
            new_name='indiceConcluintesRegiaoFederal',
        ),
        migrations.RenameField(
            model_name='fatoaluno',
            old_name='indiceIngressantesRegiaoIngressanteEstadual',
            new_name='indiceIngressantesRegiaoEstadual',
        ),
        migrations.RenameField(
            model_name='fatoaluno',
            old_name='indiceIngressantesRegiaoIngressanteFederal',
            new_name='indiceIngressantesRegiaoFederal',
        ),
    ]
