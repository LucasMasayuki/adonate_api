# Generated by Django 2.2.7 on 2019-11-15 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20191114_1859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adonator',
            name='address',
        ),
        migrations.AddField(
            model_name='campaign',
            name='address',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='app.Address'),
            preserve_default=False,
        ),
    ]
