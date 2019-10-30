# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EntityTable(models.Model):
    entity_id = models.AutoField(primary_key=True)
    class_field = models.IntegerField(db_column='class')  # Field renamed because it was a Python reserved word.
    section = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entity_table'
        unique_together = (('class_field', 'section'),)


class LectureStudent(models.Model):
    id = models.BigAutoField(primary_key=True)
    student = models.ForeignKey('StudentLogin', models.DO_NOTHING)
    lecture = models.ForeignKey('LectureTeacher', models.DO_NOTHING)
    present = models.CharField(max_length=1)
    attention_percent = models.FloatField(blank=True, null=True)
    emotion_data = models.CharField(max_length=500, blank=True, null=True)
    attention_graph_link = models.CharField(max_length=1000, blank=True, null=True)
    emotion_graph_link = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lecture_student'


class LectureTeacher(models.Model):
    lecture_id = models.BigAutoField(primary_key=True)
    teacher = models.ForeignKey('TeacherLogin', models.DO_NOTHING)
    entity = models.ForeignKey(EntityTable, models.DO_NOTHING)
    school = models.ForeignKey('SchoolDetails', models.DO_NOTHING)
    lecture_start_time = models.DateTimeField()
    lecture_end_time = models.DateTimeField()
    subject = models.CharField(max_length=50, blank=True, null=True)
    topic = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lecture_teacher'


class SchoolDetails(models.Model):
    school_id = models.AutoField(primary_key=True)
    school_name = models.CharField(max_length=200)
    city = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    pin = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_details'


class StudentDetail(models.Model):
    student = models.ForeignKey('StudentLogin', models.DO_NOTHING, unique=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    school = models.ForeignKey(SchoolDetails, models.DO_NOTHING)
    entity = models.ForeignKey(EntityTable, models.DO_NOTHING)
    phone = models.CharField(unique=True, max_length=12, blank=True, null=True)
    email = models.CharField(unique=True, max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_detail'


class StudentLogin(models.Model):
    student_id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'student_login'


class TeacherDetail(models.Model):
    teacher = models.ForeignKey('TeacherLogin', models.DO_NOTHING, unique=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    school = models.ForeignKey(SchoolDetails, models.DO_NOTHING, blank=True, null=True)
    phone = models.CharField(unique=True, max_length=12, blank=True, null=True)
    email = models.CharField(unique=True, max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teacher_detail'


class TeacherLogin(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'teacher_login'
