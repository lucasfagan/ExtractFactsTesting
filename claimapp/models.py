# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Speak(models.Model):
    claim = models.TextField()
    speaker = models.TextField(blank=True, null=True)
    score = models.TextField(blank=True, null=True)
    trans_id = models.TextField(blank=True, null=True)
    claim_id = models.TextField(primary_key=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Speak'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
