# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
from django.conf import settings


class Migration(SchemaMigration):

   # dependencies = [
   #    migrations.swappable_dependency(settings.AUTH_USER_MODEL),
   # ]
    def forwards(self, orm):
        db.create_table(u'Group', (
            ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ('name', models.CharField(unique=True, max_length=255)),
        ))
        db.send_create_signal('webpush', ['Group'])
        db.create_table(u'PushInformation', (
            ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ('group', models.ForeignKey(related_name='webpush_info', blank=True, to=orm['webpush.Group'], null=True)),
            ('subscription', models.ForeignKey(related_name='webpush_info', to=orm['webpush.SubscriptionInfo'])),
            ('user', models.ForeignKey(related_name='webpush_info', blank=True, to=orm['authentication.User'], null=True)),
        ))
        db.send_create_signal('webpush', ['PushInformation'])
        db.create_table(u'SubscriptionInfo', (
            ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ('browser', models.CharField(max_length=100)),
            ('endpoint', models.URLField(max_length=255)),
            ('auth', models.CharField(max_length=100)),
            ('p256dh', models.CharField(max_length=100)),
        ))
        db.send_create_signal('webpush', ['SubscriptionInfo'])
