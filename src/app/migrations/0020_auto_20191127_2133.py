# Generated by Django 2.2.7 on 2019-11-28 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20191126_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adonator',
            name='birth_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='adonator',
            name='cnpj',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='adonator',
            name='cpf',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='adonator',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]