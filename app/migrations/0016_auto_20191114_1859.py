# Generated by Django 2.2.7 on 2019-11-14 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20191114_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tagcampaign',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tag', to='app.Tag'),
        ),
    ]
