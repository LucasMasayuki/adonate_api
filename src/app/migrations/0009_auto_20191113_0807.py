# Generated by Django 2.2.7 on 2019-11-13 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20191113_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag_type',
            field=models.CharField(choices=[('PURPOSE', 'purpose'), ('ITEM', 'item')], max_length=255),
        ),
    ]