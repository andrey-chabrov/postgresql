# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.db import migrations, models
from postgres import settings


def load_sql_from_file(filename):
    with open(filename, 'r') as f:
        sql = f.read()
    return sql


def forwards_func(apps, schema_editor):
    filename = os.path.join(settings.BASE_DIR, 'missing_pages', 'db', 'procedures.sql')
    sql = load_sql_from_file(filename)
    schema_editor.execute(sql)


class Migration(migrations.Migration):

    dependencies = [
        ('missing_pages', '0003_auto_20151204_1238'),
    ]

    operations = [
        migrations.RunPython(forwards_func),
    ]
