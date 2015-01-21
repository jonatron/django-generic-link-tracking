# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generic_links', '0002_auto_20150121_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genericlink',
            name='url',
            field=models.URLField(max_length=255),
            preserve_default=True,
        ),
    ]
