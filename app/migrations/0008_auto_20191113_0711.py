# Generated by Django 2.2.7 on 2019-11-13 10:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20191113_0708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='adonator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='adonator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='photo',
            name='campaign',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='camapaign', to='app.Campaign'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='item', to='app.Item'),
        ),
    ]
