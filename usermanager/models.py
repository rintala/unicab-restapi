
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.gis.db import models as gismodels

from django.core.validators import MaxValueValidator, MinValueValidator


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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
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


class Trips(models.Model):
    #id = models.IntegerField(primary_key=True)
    destination_home = models.NullBooleanField()
    date = models.CharField(max_length=15, blank=True, null=True)
    passenger_1 = models.ForeignKey('Users', models.DO_NOTHING, db_column='passenger_1', blank=True, null=True, related_name='passenger_1')
    passenger_2 = models.ForeignKey('Users', models.DO_NOTHING, db_column='passenger_2', blank=True, null=True, related_name='passenger_2')
    passenger_3 = models.ForeignKey('Users', models.DO_NOTHING, db_column='passenger_3', blank=True, null=True, related_name='passenger_3')
    total_cost = models.FloatField(blank=True, null=True)
    description = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trips'


class UsermanagerUsers(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    first_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'usermanager_users'


class Users(models.Model):
    #id = models.IntegerField(primary_key=True)
    #id = models.SerialField(primary_key=True, editable=False, help_text=_("Auto Increment Number"), verbose_name=_("Number"),)
    #id = models.AutoField(primary_key=True),
    first_name = models.CharField(max_length=15, blank=True, null=True)
    last_name = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=35)
    date_of_birth = models.DateField(blank=True, null=True)
    phone_nr = models.CharField(max_length=15, blank=True, null=True)
    phone_verified = models.BooleanField()
    faculty = models.CharField(max_length=15, blank=True, null=True)
    #home_adress = models.CharField(max_length=20, blank=True, null=True)
    home_latitude = models.DecimalField(max_digits=10, decimal_places=6)
    home_longitude = models.DecimalField(max_digits=10, decimal_places=6)
    nr_of_trips_done = models.IntegerField(blank=True, default=0)
    avg_rating = models.FloatField(blank=True, null=True, validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ])
    profile_picture = models.CharField(max_length=15, blank=True, null=True)
    description = models.CharField(max_length=35, blank=True, null=True)
    is_searching = models.BooleanField(default=False, null=False)

    class Meta:
        managed = False
        db_table = 'users'
