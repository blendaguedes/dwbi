# Generated by Django 2.2.7 on 2019-11-26 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0010_auto_20191126_0820'),
    ]

    operations = [
        migrations.AddField(
            model_name='fatoaluno',
            name='indiceDesistenciaResevaVagasRegiao',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
