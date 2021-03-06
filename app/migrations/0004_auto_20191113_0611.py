# Generated by Django 2.2.7 on 2019-11-13 09:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20191113_0123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campaign',
            old_name='date_end',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='campaign',
            old_name='date_start',
            new_name='start',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='item_type_tag',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='purpose_tag',
        ),
        migrations.AlterField(
            model_name='adonator',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app.Address'),
        ),
        migrations.AlterField(
            model_name='adonatorgalery',
            name='adonator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='adonatorgalery',
            name='photo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='app.Photo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='campaign',
            name='adonator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='campaigngalery',
            name='campaign',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='app.Campaign'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='campaigngalery',
            name='photo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='app.Photo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='donation',
            name='adonator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='donation',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='app.Item'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='donationcampaign',
            name='campaingn',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='app.Campaign'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='donationcampaign',
            name='donation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='app.Donation'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='itemgalery',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='app.Item'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='itemgalery',
            name='photo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='app.Photo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='report',
            name='adonator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='report',
            name='campaign',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='app.Campaign'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='TagCampaign',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('campaign', models.CharField(max_length=200)),
                ('tag_type', models.CharField(choices=[('PORUPUSE', 'pourpuse'), ('ITEM', 'item')], max_length=255)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Tag')),
            ],
            options={
                'verbose_name': 'TagCampaign',
                'verbose_name_plural': 'TagsCampaigns',
                'db_table': 'tag_campaign',
            },
        ),
    ]
