# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Expense.head'
        db.delete_column(u'expenses_expense', 'head')

        # Deleting field 'Expense.pay_mode'
        db.delete_column(u'expenses_expense', 'pay_mode')

        # Adding field 'Expense.payment_mode'
        db.add_column(u'expenses_expense', 'payment_mode',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Expense.narration'
        db.add_column(u'expenses_expense', 'narration',
                      self.gf('django.db.models.fields.TextField')(max_length=300, null=True, blank=True),
                      keep_default=False)

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Expense.head'
        raise RuntimeError("Cannot reverse this migration. 'Expense.head' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Expense.pay_mode'
        raise RuntimeError("Cannot reverse this migration. 'Expense.pay_mode' and its values cannot be restored.")
        # Deleting field 'Expense.payment_mode'
        db.delete_column(u'expenses_expense', 'payment_mode')

        # Deleting field 'Expense.narration'
        db.delete_column(u'expenses_expense', 'narration')

    models = {
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
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'expenses.expense': {
            'Meta': {'object_name': 'Expense'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'bank_name': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'branch': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'cheque_date': ('django.db.models.fields.DateField', [], {}),
            'cheque_no': ('django.db.models.fields.IntegerField', [], {}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'expense_head': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['expenses.ExpenseHead']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'narration': ('django.db.models.fields.TextField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'payment_mode': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'voucher_no': ('django.db.models.fields.IntegerField', [], {})
        },
        u'expenses.expensehead': {
            'Meta': {'object_name': 'ExpenseHead'},
            'expense_head': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['expenses']