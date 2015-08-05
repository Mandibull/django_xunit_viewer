# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('xunit_output_path', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('xml_file', models.TextField()),
                ('json_results', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(to='xunit_viewer.Project')),
            ],
        ),
    ]
