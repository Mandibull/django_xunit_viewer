# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xunit_viewer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testresult',
            options={'ordering': ('date',)},
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='json_results',
            field=models.TextField(null=True),
        ),
    ]
