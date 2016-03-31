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
            name='Policy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='What should this policy be called?', max_length=50)),
                ('lock', models.BooleanField(default=False, editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Revision',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('preamble', models.TextField(blank=True)),
                ('position', models.TextField(blank=True)),
                ('action', models.TextField(blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('change', models.CharField(max_length=50)),
                ('endorsers', models.ManyToManyField(related_name='endorsers', to=settings.AUTH_USER_MODEL)),
                ('policy', models.ForeignKey(to='policy.Policy')),
                ('submitters', models.ManyToManyField(related_name='submitters', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RevisionStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(help_text="What's the new status?", max_length=2, choices=[('SB', 'Submitted'), ('AG', 'In Agenda'), ('DL', 'Discussion Delayed'), ('EN', 'Enacted'), ('FA', 'Failed'), ('NU', 'Nullified'), ('IV', 'Invalid')])),
                ('notes', models.CharField(max_length=50)),
                ('changer', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, help_text='Who caused the status change?')),
                ('revision', models.ForeignKey(to='policy.Revision')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
