# Generated by Django 2.2.6 on 2019-10-22 07:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('zipcode', models.IntegerField(blank=True, default=None, null=True)),
                ('street', models.CharField(max_length=200)),
                ('number', models.IntegerField(blank=True, default=None, null=True)),
                ('state', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'addresses',
            },
        ),
        migrations.CreateModel(
            name='Campaigns',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('users_id', models.IntegerField(default=None, null=True, verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Users'))),
                ('item_type_tag_id', models.IntegerField(default=None, null=True, verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Tags'))),
                ('purpose_tag_id', models.IntegerField(default=None, null=True, verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Tags'))),
                ('campaigns_galeries_id', models.IntegerField(default=None, null=True, verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CampaignsGaleries'))),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'campaigns',
            },
        ),
        migrations.CreateModel(
            name='CampaignsGaleries',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('campaigns_id', models.IntegerField(default=None, null=True, verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Campaigns'))),
                ('photos_id', models.IntegerField(default=None, null=True, verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Photos'))),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'campaigns_galeries',
            },
        ),
        migrations.CreateModel(
            name='Donations',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('users_id', models.IntegerField(default=None, null=True, verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Users'))),
                ('items_id', models.IntegerField(default=None, null=True, verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Items'))),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'donations',
            },
        ),
        migrations.CreateModel(
            name='DonationsCampaigns',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('campaingns_id', models.IntegerField(default=None, null=True, verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Campaigns'))),
                ('donations_id', models.IntegerField(default=None, null=True, verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Donations'))),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'donations_campaigns',
            },
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('items_galeries_id', models.IntegerField(default=None, null=True, verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ItemsGaleries'))),
                ('name', models.CharField(default='', max_length=200)),
                ('amount', models.IntegerField(default=0)),
                ('coments', models.CharField(max_length=200)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'items',
            },
        ),
        migrations.CreateModel(
            name='ItemsGaleries',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('items_id', models.IntegerField(default=None, null=True, verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Items'))),
                ('photos_id', models.IntegerField(default=None, null=True, verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Photos'))),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'items_galeries',
            },
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('photo', models.CharField(max_length=200)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'photos',
            },
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('users_id', models.IntegerField(default=None, null=True, verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Users'))),
                ('campaigns_id', models.IntegerField(default=None, null=True, verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Campaigns'))),
                ('text', models.CharField(max_length=200)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'reports',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'tags',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('users_galeries_id', models.IntegerField(default=None, null=True, verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='UsersGaleries'))),
                ('addresses_id', models.IntegerField(default=None, null=True, verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Addresses'))),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('cpf', models.CharField(default=None, max_length=200, null=True)),
                ('cnpj', models.CharField(default=None, max_length=200, null=True)),
                ('birth_date', models.DateField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='UsersGaleries',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('users_id', models.IntegerField(default=None, null=True, verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Users'))),
                ('photos_id', models.IntegerField(default=None, null=True, verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Photos'))),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'users_campaigns',
            },
        ),
    ]