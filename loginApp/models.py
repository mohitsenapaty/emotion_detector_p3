# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Userprofile(models.Model):
    createdat = models.CharField(db_column='createdAt', max_length=-1, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.CharField(db_column='updatedAt', max_length=-1, blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField()
    userid = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    firstname = models.TextField(blank=True, null=True)
    lastname = models.TextField(blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    refid = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userprofile'
