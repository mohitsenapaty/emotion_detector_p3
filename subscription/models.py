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
    type = models.TextField(blank=True, null=True)
    subscribedon = models.TextField(blank=True, null=True)
    renewalstatus = models.TextField(blank=True, null=True)
    autorenewal = models.TextField(blank=True, null=True)
    feepaid = models.IntegerField(blank=True, null=True)
    discount = models.IntegerField(blank=True, null=True)
    discountcode = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coursesubscription'

