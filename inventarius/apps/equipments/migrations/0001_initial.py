# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BackupConf',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=75, editable=False)),
                ('log_conf', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=75)),
                ('slug', models.SlugField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('model', models.CharField(max_length=150)),
                ('ip_conf', models.GenericIPAddressField(default=None, null=True, blank=True)),
                ('mask_conf', models.GenericIPAddressField(default=None, null=True, blank=True)),
                ('ip_swi', models.GenericIPAddressField(default=None, null=True, blank=True)),
                ('mask_swi', models.GenericIPAddressField(default=None, null=True, blank=True)),
                ('image', models.ImageField(upload_to=b'equipments')),
                ('is_active', models.BooleanField(default=True)),
                ('admin_user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('brand', models.ForeignKey(to='equipments.Brand')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='backupconf',
            name='equipment',
            field=models.ForeignKey(to='equipments.Equipment'),
        ),
    ]
