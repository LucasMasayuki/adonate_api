# Generated by Django 2.2.7 on 2019-11-27 02:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20191115_0536'),
    ]

    operations = [
        migrations.AddField(
            model_name='adonator',
            name='name',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='adonator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='adonator', to=settings.AUTH_USER_MODEL),
        ),
    ]