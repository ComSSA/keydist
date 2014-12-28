# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Policy'
        db.create_table(u'policy_policy', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('lock', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'policy', ['Policy'])

        # Adding model 'Revision'
        db.create_table(u'policy_revision', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('preamble', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('position', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('action', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('policy', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['policy.Policy'])),
        ))
        db.send_create_signal(u'policy', ['Revision'])

        # Adding M2M table for field submitters on 'Revision'
        m2m_table_name = db.shorten_name(u'policy_revision_submitters')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('revision', models.ForeignKey(orm[u'policy.revision'], null=False)),
            ('keydistuser', models.ForeignKey(orm[u'accounts.keydistuser'], null=False))
        ))
        db.create_unique(m2m_table_name, ['revision_id', 'keydistuser_id'])

        # Adding M2M table for field endorsers on 'Revision'
        m2m_table_name = db.shorten_name(u'policy_revision_endorsers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('revision', models.ForeignKey(orm[u'policy.revision'], null=False)),
            ('keydistuser', models.ForeignKey(orm[u'accounts.keydistuser'], null=False))
        ))
        db.create_unique(m2m_table_name, ['revision_id', 'keydistuser_id'])

        # Adding model 'RevisionStatus'
        db.create_table(u'policy_revisionstatus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('changer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.KeydistUser'])),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('revision', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['policy.Revision'])),
        ))
        db.send_create_signal(u'policy', ['RevisionStatus'])


    def backwards(self, orm):
        # Deleting model 'Policy'
        db.delete_table(u'policy_policy')

        # Deleting model 'Revision'
        db.delete_table(u'policy_revision')

        # Removing M2M table for field submitters on 'Revision'
        db.delete_table(db.shorten_name(u'policy_revision_submitters'))

        # Removing M2M table for field endorsers on 'Revision'
        db.delete_table(db.shorten_name(u'policy_revision_endorsers'))

        # Deleting model 'RevisionStatus'
        db.delete_table(u'policy_revisionstatus')


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
        u'policy.policy': {
            'Meta': {'object_name': 'Policy'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lock': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'policy.revision': {
            'Meta': {'object_name': 'Revision'},
            'action': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'endorsers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'endorsers'", 'symmetrical': 'False', 'to': u"orm['accounts.KeydistUser']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'policy': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['policy.Policy']"}),
            'position': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'preamble': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'submitters': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'submitters'", 'symmetrical': 'False', 'to': u"orm['accounts.KeydistUser']"})
        },
        u'policy.revisionstatus': {
            'Meta': {'object_name': 'RevisionStatus'},
            'changer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.KeydistUser']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'revision': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['policy.Revision']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['policy']