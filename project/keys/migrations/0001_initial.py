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
            name='Key',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(help_text=b'The key text.', max_length=140)),
                ('key_type', models.CharField(help_text=b'The type of key, as reported by the MSDNAA portal.', max_length=50)),
                ('allocated_at', models.DateTimeField(help_text=b'The time and date at which the key was allocated, if at all.', null=True, blank=True)),
                ('imported_at', models.DateTimeField(help_text=b'The date and time at which the key was imported.')),
                ('allocated_by', models.ForeignKey(related_name='allocated_by', blank=True, to=settings.AUTH_USER_MODEL, help_text=b'The user that allocated this key.', null=True)),
                ('allocated_to', models.ForeignKey(related_name='allocated_to', blank=True, to=settings.AUTH_USER_MODEL, help_text=b'The user the key has been allocated to.', null=True)),
                ('imported_by', models.ForeignKey(related_name='imported_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'The name of the product.', unique=True, max_length=50)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SKU',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'The name of the SKU.', unique=True, max_length=140)),
                ('product', models.ForeignKey(to='keys.Product')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'SKU',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='key',
            name='sku',
            field=models.ForeignKey(to='keys.SKU'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='key',
            unique_together=set([('key', 'sku')]),
        ),
    ]
