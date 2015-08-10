# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xunit_viewer', '0002_auto_20150805_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testresult',
            name='json_results',
            field=models.TextField(null=True, blank=True),
        ),
    ]
