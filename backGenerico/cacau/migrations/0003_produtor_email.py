# Generated by Django 5.1.1 on 2024-10-19 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cacau', '0002_cadastro_endereco_lote_producao_fermentacao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtor',
            name='email',
            field=models.EmailField(default=-3, max_length=254),
            preserve_default=False,
        ),
    ]
