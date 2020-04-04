from django.db import models
import loginApp.models as loginModels

# Create your models here.
class Courses(models.Model):
    createdat = models.CharField(db_column='createdAt', max_length=40, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.CharField(db_column='updatedAt', max_length=40, blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(primary_key=True, db_column='id')
    courseid = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    subject = models.TextField(blank=True, null=True)
    designedfor = models.TextField(blank=True, null=True)
    courseof = models.ForeignKey(loginModels.Userprofile, on_delete=models.SET_NULL, blank=True, null=True, db_column='courseof', related_name='courseof')
    subscriptionfee = models.IntegerField(blank=True, null=True) #base course fee per lecture
    numlectures = models.IntegerField(blank=True, null=True)
    startdate = models.CharField(max_length=40, blank=True, null=True)
    numsubscribers = models.IntegerField(blank=True, null=True)
    lastupdated = models.CharField(max_length=40, blank=True, null=True)
    status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'courses'
        
        
class Lectures(models.Model):
    createdat = models.CharField(db_column='createdAt', max_length=40, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.CharField(db_column='updatedAt', max_length=40, blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(primary_key=True)
    lectureid = models.TextField(blank=True, null=True)
    courseid = models.ForeignKey(Courses, on_delete=models.SET_NULL, blank=True, null=True, db_column='courseid', related_name='courseids')
    lectureof = models.ForeignKey(loginModels.Userprofile, on_delete=models.SET_NULL,blank=True, null=True, db_column='lectureof', related_name='lectureof')
    type = models.TextField(blank=True, null=True)
    topic = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    startdateandtime = models.CharField(max_length=40, blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    validitystatus = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    vidcontentlink = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lectures'


