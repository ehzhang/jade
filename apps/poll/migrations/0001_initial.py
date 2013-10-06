# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Poll'
        db.create_table(u'poll_poll', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('timestamp', self.gf('django.db.models.fields.TimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'poll', ['Poll'])

        # Adding model 'Option'
        db.create_table(u'poll_option', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('poll', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['poll.Poll'])),
            ('public_id', self.gf('django.db.models.fields.IntegerField')()),
            ('submitter', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('timestamp', self.gf('django.db.models.fields.TimeField')(auto_now_add=True, blank=True)),
            ('upvotes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('downvotes', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'poll', ['Option'])

        # Adding model 'Comment'
        db.create_table(u'poll_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('option', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['poll.Option'])),
            ('public_id', self.gf('django.db.models.fields.IntegerField')()),
            ('submitter', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('timestamp', self.gf('django.db.models.fields.TimeField')(auto_now_add=True, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('upvotes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('downvotes', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'poll', ['Comment'])


    def backwards(self, orm):
        # Deleting model 'Poll'
        db.delete_table(u'poll_poll')

        # Deleting model 'Option'
        db.delete_table(u'poll_option')

        # Deleting model 'Comment'
        db.delete_table(u'poll_comment')


    models = {
        u'poll.comment': {
            'Meta': {'object_name': 'Comment'},
            'downvotes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'option': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['poll.Option']"}),
            'public_id': ('django.db.models.fields.IntegerField', [], {}),
            'submitter': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'timestamp': ('django.db.models.fields.TimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'upvotes': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'poll.option': {
            'Meta': {'object_name': 'Option'},
            'downvotes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poll': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['poll.Poll']"}),
            'public_id': ('django.db.models.fields.IntegerField', [], {}),
            'submitter': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'timestamp': ('django.db.models.fields.TimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'upvotes': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'poll.poll': {
            'Meta': {'object_name': 'Poll'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'timestamp': ('django.db.models.fields.TimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['poll']