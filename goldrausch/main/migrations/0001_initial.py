# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Agent'
        db.create_table('main_agent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('secret', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('code', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('main', ['Agent'])

        # Adding model 'Task'
        db.create_table('main_task', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('aegnt', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tasks', to=orm['main.Agent'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('code', self.gf('django.db.models.fields.IntegerField')()),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('main', ['Task'])


    def backwards(self, orm):
        # Deleting model 'Agent'
        db.delete_table('main_agent')

        # Deleting model 'Task'
        db.delete_table('main_task')


    models = {
        'main.agent': {
            'Meta': {'object_name': 'Agent'},
            'code': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'main.task': {
            'Meta': {'object_name': 'Task'},
            'aegnt': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tasks'", 'to': "orm['main.Agent']"}),
            'code': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['main']