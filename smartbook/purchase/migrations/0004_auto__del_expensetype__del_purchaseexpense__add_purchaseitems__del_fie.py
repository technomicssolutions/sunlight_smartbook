# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'ExpenseType'
        db.delete_table(u'purchase_expensetype')

        # Deleting model 'PurchaseExpense'
        db.delete_table(u'purchase_purchaseexpense')

        # Adding model 'PurchaseItems'
        db.create_table(u'purchase_purchaseitems', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Item'], null=True, blank=True)),
            ('purchase', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['purchase.Purchase'], null=True, blank=True)),
            ('item_frieght', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('frieght_per_unit', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('item_handling', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('handling_per_unit', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('expense', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('expense_per_unit', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('net_amount', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=14, decimal_places=3)),
            ('vendor_amount', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=14, decimal_places=3)),
        ))
        db.send_create_signal(u'purchase', ['PurchaseItems'])

        # Deleting field 'Purchase.selling_price'
        db.delete_column(u'purchase_purchase', 'selling_price')

        # Deleting field 'Purchase.date'
        db.delete_column(u'purchase_purchase', 'date')

        # Deleting field 'Purchase.invoice_number'
        db.delete_column(u'purchase_purchase', 'invoice_number')

        # Deleting field 'Purchase.item'
        db.delete_column(u'purchase_purchase', 'item_id')

        # Deleting field 'Purchase.time'
        db.delete_column(u'purchase_purchase', 'time')

        # Deleting field 'Purchase.cost_price'
        db.delete_column(u'purchase_purchase', 'cost_price')

        # Deleting field 'Purchase.quantity'
        db.delete_column(u'purchase_purchase', 'quantity')

        # Adding field 'Purchase.purchase_invoice_number'
        db.add_column(u'purchase_purchase', 'purchase_invoice_number',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Purchase.vendor_invoice_number'
        db.add_column(u'purchase_purchase', 'vendor_invoice_number',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Purchase.vendor_do_number'
        db.add_column(u'purchase_purchase', 'vendor_do_number',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Purchase.vendor_invoice_date'
        db.add_column(u'purchase_purchase', 'vendor_invoice_date',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Purchase.purchase_invoice_date'
        db.add_column(u'purchase_purchase', 'purchase_invoice_date',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Purchase.transportation_company'
        db.add_column(u'purchase_purchase', 'transportation_company',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.TransportationCompany'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Purchase.discount'
        db.add_column(u'purchase_purchase', 'discount',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=14, decimal_places=3),
                      keep_default=False)


        # Changing field 'Purchase.brand'
        db.alter_column(u'purchase_purchase', 'brand_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Brand'], null=True))

        # Changing field 'Purchase.vendor'
        db.alter_column(u'purchase_purchase', 'vendor_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Vendor'], null=True))
    def backwards(self, orm):
        # Adding model 'ExpenseType'
        db.create_table(u'purchase_expensetype', (
            ('category', self.gf('django.db.models.fields.CharField')(max_length=50)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'purchase', ['ExpenseType'])

        # Adding model 'PurchaseExpense'
        db.create_table(u'purchase_purchaseexpense', (
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['purchase.ExpenseType'])),
            ('purchase', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['purchase.Purchase'])),
            ('paid', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=14, decimal_places=2)),
            ('total', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=14, decimal_places=2)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'purchase', ['PurchaseExpense'])

        # Deleting model 'PurchaseItems'
        db.delete_table(u'purchase_purchaseitems')

        # Adding field 'Purchase.selling_price'
        db.add_column(u'purchase_purchase', 'selling_price',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=14, decimal_places=2),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Purchase.date'
        raise RuntimeError("Cannot reverse this migration. 'Purchase.date' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Purchase.invoice_number'
        raise RuntimeError("Cannot reverse this migration. 'Purchase.invoice_number' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Purchase.item'
        raise RuntimeError("Cannot reverse this migration. 'Purchase.item' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Purchase.time'
        raise RuntimeError("Cannot reverse this migration. 'Purchase.time' and its values cannot be restored.")
        # Adding field 'Purchase.cost_price'
        db.add_column(u'purchase_purchase', 'cost_price',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=14, decimal_places=2),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Purchase.quantity'
        raise RuntimeError("Cannot reverse this migration. 'Purchase.quantity' and its values cannot be restored.")
        # Deleting field 'Purchase.purchase_invoice_number'
        db.delete_column(u'purchase_purchase', 'purchase_invoice_number')

        # Deleting field 'Purchase.vendor_invoice_number'
        db.delete_column(u'purchase_purchase', 'vendor_invoice_number')

        # Deleting field 'Purchase.vendor_do_number'
        db.delete_column(u'purchase_purchase', 'vendor_do_number')

        # Deleting field 'Purchase.vendor_invoice_date'
        db.delete_column(u'purchase_purchase', 'vendor_invoice_date')

        # Deleting field 'Purchase.purchase_invoice_date'
        db.delete_column(u'purchase_purchase', 'purchase_invoice_date')

        # Deleting field 'Purchase.transportation_company'
        db.delete_column(u'purchase_purchase', 'transportation_company_id')

        # Deleting field 'Purchase.discount'
        db.delete_column(u'purchase_purchase', 'discount')


        # User chose to not deal with backwards NULL issues for 'Purchase.brand'
        raise RuntimeError("Cannot reverse this migration. 'Purchase.brand' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Purchase.vendor'
        raise RuntimeError("Cannot reverse this migration. 'Purchase.vendor' and its values cannot be restored.")
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
        u'inventory.brand': {
            'Meta': {'object_name': 'Brand'},
            'brand': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '51'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'inventory.item': {
            'Meta': {'object_name': 'Item'},
            'barcode': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'brand': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Brand']"}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'tax': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '14', 'decimal_places': '2'}),
            'uom': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.UnitOfMeasure']"})
        },
        u'inventory.unitofmeasure': {
            'Meta': {'object_name': 'UnitOfMeasure'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'uom': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'purchase.purchase': {
            'Meta': {'object_name': 'Purchase'},
            'brand': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Brand']", 'null': 'True', 'blank': 'True'}),
            'discount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '14', 'decimal_places': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'purchase_invoice_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'purchase_invoice_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'transportation_company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.TransportationCompany']", 'null': 'True', 'blank': 'True'}),
            'vendor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Vendor']", 'null': 'True', 'blank': 'True'}),
            'vendor_do_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'vendor_invoice_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'vendor_invoice_number': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'purchase.purchaseitems': {
            'Meta': {'object_name': 'PurchaseItems'},
            'expense': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'expense_per_unit': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'frieght_per_unit': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'handling_per_unit': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Item']", 'null': 'True', 'blank': 'True'}),
            'item_frieght': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'item_handling': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'net_amount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '14', 'decimal_places': '3'}),
            'purchase': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['purchase.Purchase']", 'null': 'True', 'blank': 'True'}),
            'vendor_amount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '14', 'decimal_places': '3'})
        },
        u'purchase.purchasereturn': {
            'Meta': {'object_name': 'PurchaseReturn'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'purchase': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['purchase.Purchase']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'time': ('django.db.models.fields.TimeField', [], {})
        },
        u'web.transportationcompany': {
            'Meta': {'object_name': 'TransportationCompany'},
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'web.vendor': {
            'Meta': {'object_name': 'Vendor'},
            'contact_person': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['purchase']