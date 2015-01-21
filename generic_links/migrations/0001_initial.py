# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenericLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('where', models.CharField(default=b'', max_length=200, blank=True)),
                ('url', models.CharField(max_length=255, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('show_in_admin', models.BooleanField(default=True)),
                ('rotate', models.CharField(max_length=100, blank=True)),
                ('object_id', models.PositiveIntegerField(null=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GenericLinkClick',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.IPAddressField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('link', models.ForeignKey(to='generic_links.GenericLink')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
