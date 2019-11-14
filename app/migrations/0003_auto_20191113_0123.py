# Generated by Django 2.2.7 on 2019-11-13 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20191101_0442'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campaigngalery',
            old_name='photos',
            new_name='photo',
        ),
        migrations.RemoveField(
            model_name='adonator',
            name='adonator_galery',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='adonater',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='campaign_galery',
        ),
        migrations.RemoveField(
            model_name='item',
            name='item_galery',
        ),
        migrations.RemoveField(
            model_name='report',
            name='adonater',
        ),
        migrations.AddField(
            model_name='address',
            name='lat',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='lng',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='campaign',
            name='adonator',
            field=models.IntegerField(default=None, null=True, verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Adonator')),
        ),
        migrations.AddField(
            model_name='report',
            name='adonator',
            field=models.IntegerField(default=None, null=True, verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Adonator')),
        ),
    ]
