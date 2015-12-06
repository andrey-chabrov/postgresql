# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('missing_pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('index', models.IntegerField()),
            ],
            options={
                'ordering': ('version__name',),
            },
        ),
        migrations.CreateModel(
            name='StudentPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField()),
                ('page', models.ForeignKey(to='missing_pages.Page')),
                ('student', models.ForeignKey(to='missing_pages.Student')),
            ],
            options={
                'ordering': ('student', 'page__version__name'),
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('test', models.ForeignKey(to='missing_pages.Test')),
            ],
            options={
                'ordering': ('test__name',),
            },
        ),
        migrations.AddField(
            model_name='page',
            name='version',
            field=models.ForeignKey(to='missing_pages.Version'),
        ),
        migrations.AlterUniqueTogether(
            name='version',
            unique_together=set([('test', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='studentpage',
            unique_together=set([('page', 'student')]),
        ),
        migrations.AlterUniqueTogether(
            name='page',
            unique_together=set([('version', 'index')]),
        ),
    ]
