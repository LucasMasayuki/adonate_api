# Generated by Django 2.2.7 on 2019-11-15 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20191115_0516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='address', to='app.Address'),
        ),
    ]
