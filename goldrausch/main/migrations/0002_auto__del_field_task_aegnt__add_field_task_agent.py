# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Task.aegnt'
        db.delete_column('main_task', 'aegnt_id')

        # Adding field 'Task.agent'
        db.add_column('main_task', 'agent',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='tasks', to=orm['main.Agent']),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Task.aegnt'
        raise RuntimeError("Cannot reverse this migration. 'Task.aegnt' and its values cannot be restored.")
        # Deleting field 'Task.agent'
        db.delete_column('main_task', 'agent_id')


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
            'agent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tasks'", 'to': "orm['main.Agent']"}),
            'code': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['main']