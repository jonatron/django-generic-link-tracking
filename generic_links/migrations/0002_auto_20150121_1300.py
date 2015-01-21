# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generic_links', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genericlink',
            name='content_type',
            field=models.ForeignKey(blank=True, to='contenttypes.ContentType', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='genericlink',
            name='object_id',
            field=models.PositiveIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='genericlink',
            name='url',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
    ]
