# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Product'
        db.create_table(u'keys_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'keys', ['Product'])

        # Adding model 'SKU'
        db.create_table(u'keys_sku', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['keys.Product'])),
        ))
        db.send_create_signal(u'keys', ['SKU'])

        # Adding model 'Key'
        db.create_table(u'keys_key', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('key_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('claimed', self.gf('django.db.models.fields.DateField')()),
            ('allocated_to', self.gf('django.db.models.fields.related.ForeignKey')(related_name='allocated_to', blank=True, to=orm['accounts.KeydistUser'])),
            ('allocated_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='allocated_by', blank=True, to=orm['accounts.KeydistUser'])),
            ('allocated_at', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('sku', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['keys.SKU'])),
        ))
        db.send_create_signal(u'keys', ['Key'])


    def backwards(self, orm):
        # Deleting model 'Product'
        db.delete_table(u'keys_product')

        # Deleting model 'SKU'
        db.delete_table(u'keys_sku')

        # Deleting model 'Key'
        db.delete_table(u'keys_key')


    models = {
        u'accounts.keydistuser': {
            'Meta': {'ordering': "['first_name']", 'object_name': 'KeydistUser'},
            'curtin_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'keys.key': {
            'Meta': {'object_name': 'Key'},
            'allocated_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'allocated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'allocated_by'", 'blank': 'True', 'to': u"orm['accounts.KeydistUser']"}),
            'allocated_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'allocated_to'", 'blank': 'True', 'to': u"orm['accounts.KeydistUser']"}),
            'claimed': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'key_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sku': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['keys.SKU']"})
        },
        u'keys.product': {
            'Meta': {'object_name': 'Product'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'keys.sku': {
            'Meta': {'object_name': 'SKU'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['keys.Product']"})
        }
    }

    complete_apps = ['keys']