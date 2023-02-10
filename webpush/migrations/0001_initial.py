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

