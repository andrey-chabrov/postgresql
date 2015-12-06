# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('missing_pages', '0002_auto_20151203_1319'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ('version__test__name', 'version__name', 'index')},
        ),
        migrations.AlterModelOptions(
            name='studentpage',
            options={'ordering': ('student__name', 'page__version__test__name', 'page__version__name', 'page__index')},
        ),
    ]
