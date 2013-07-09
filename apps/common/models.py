import datetime

from django.db import models
from apps.account.models import User


class Base(models.Model):
    created_on = models.DateTimeField(blank=True, null=True, auto_now_add=True, editable=False)
    # We need this to not have reverse relation, since there will be field name clashes
    created_by = models.ForeignKey(User, blank=True, null=True, related_name='+', editable=False)
    created_from = models.CharField(max_length=15, blank=True, null=True, editable=False)

    last_modified_on = models.DateTimeField(blank=True, null=True, default=datetime.datetime.now(), editable=False)
    # We need this to not have reverse relation, since there will be field name clashes
    last_modified_by = models.ForeignKey(User, blank=True, null=True, related_name='+', editable=False)
    last_modified_from = models.CharField(max_length=15, blank=True, null=True, editable=False)

    class Meta:
        abstract = True