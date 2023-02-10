# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
from django.conf import settings


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'UserEventEscalation.escalation_user_type'
        db.add_column(u'webpush_PushInformation', 'subscription',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='webpush_info', to=orm['webpush.SubscriptionInfo']),
                      keep_default=False)
        db.add_column(u'webpush_PushInformation', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='webpush_info', to=orm['authentication.User'], null=True),
                      keep_default=False)
