from django.db import models
import loginApp.models as loginModels
import teacherfunctions.models as tfModels
import subscription.models as submodels
# Create your models here.

class Paymentrequest(models.Model):
    createdat = models.CharField(db_column='createdAt', max_length=-1, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.CharField(db_column='updatedAt', max_length=-1, blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField()
    requestid = models.TextField(blank=True, null=True)
    userid = models.ForeignKey(loginModels.Userprofile, on_delete=models.SET_NULL,blank=True, null=True, db_column='userid', related_name='userids1')
    recordedon = models.TextField(blank=True, null=True)
    pgresponse = models.TextField(blank=True, null=True)  # This field type is a guess.
    amount = models.IntegerField(blank=True, null=True)
    discount = models.IntegerField(blank=True, null=True)
    discountcode = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paymentrequest'

class Subsciptionpayment(models.Model):
    createdat = models.CharField(db_column='createdAt', max_length=-1, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.CharField(db_column='updatedAt', max_length=-1, blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField()
    request = models.IntegerField()
    subscription = models.IntegerField()
    amount = models.IntegerField(blank=True, null=True)
    discount = models.IntegerField(blank=True, null=True)
    discountcode = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subsciptionpayment'
