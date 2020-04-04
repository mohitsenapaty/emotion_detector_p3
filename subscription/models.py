from django.db import models
import loginApp.models as loginModels
import teacherfunctions.models as tfModels

# Create your models here.
class Coursesubscription(models.Model):
    createdat = models.CharField(db_column='createdAt', max_length=40, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.CharField(db_column='updatedAt', max_length=40, blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(primary_key=True)
    subscriptionid = models.TextField(blank=True, null=True)
    userid = models.ForeignKey(loginModels.Userprofile, on_delete=models.SET_NULL,blank=True, null=True, db_column='userid', related_name='userids1')
    courseid = models.ForeignKey(tfModels.Courses, on_delete=models.SET_NULL, blank=True, null=True, db_column='courseid', related_name='courseids1')
    courseof = models.ForeignKey(loginModels.Userprofile, on_delete=models.SET_NULL,blank=True, null=True, db_column='courseof', related_name='courseof1')
    subscribedon = models.TextField(blank=True, null=True)
    feepaid = models.IntegerField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coursesubscription'


class Plan(models.Model):
    createdat = models.CharField(db_column='createdAt', max_length=40, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.CharField(db_column='updatedAt', max_length=40, blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(primary_key=True)
    planid = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    discountpercent = models.IntegerField(blank=True, null=True) #discount percent
    basemultiplier = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    courseid = models.ForeignKey(tfModels.Courses, on_delete=models.SET_NULL, blank=True, null=True, db_column='courseid', related_name='courseids2')
    class_field = models.TextField(db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    addedon = models.TextField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plan'

'''
basic plans will be daily -> daily, monthly, quarterly, halfyearly, yearly
custom plans will have custom discount percent
'''

