# Generated by Django 4.1.5 on 2023-01-27 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0005_alter_pacientes_idade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacientes',
            name='idade',
            field=models.CharField(max_length=19),
        ),
    ]
