# Generated by Django 2.2.7 on 2019-11-28 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20191127_2133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adonator',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='adonator',
            name='cnpj',
        ),
        migrations.RemoveField(
            model_name='adonator',
            name='cpf',
        ),
    ]
