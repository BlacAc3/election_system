# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agentname(models.Model):
    name_id = models.AutoField(primary_key=True)
    firstname = models.TextField()
    lastname = models.TextField()
    email = models.TextField(blank=True, null=True)
    phone = models.TextField()
    pollingunit_uniqueid = models.IntegerField()

    class Meta:
        managed = False  
        db_table = 'agentname'


class AnnouncedLgaResults(models.Model):
    result_id = models.AutoField(primary_key=True)   
    lga_name = models.TextField()
    party_abbreviation = models.TextField()
    party_score = models.IntegerField()
    entered_by_user = models.TextField()
    date_entered = models.TextField()
    user_ip_address = models.TextField()

    class Meta:
        managed = False  
        db_table = 'announced_lga_results'


class AnnouncedPuResults(models.Model):
    result_id = models.AutoField(primary_key=True)
    polling_unit_uniqueid = models.TextField()
    party_abbreviation = models.TextField()
    party_score = models.IntegerField()
    entered_by_user = models.TextField()
    date_entered = models.TextField()
    user_ip_address = models.TextField()

    class Meta:
        managed = False  
        db_table = 'announced_pu_results'


class AnnouncedStateResults(models.Model):
    result_id = models.AutoField(primary_key=True)
    state_name = models.TextField()
    party_abbreviation = models.TextField()
    party_score = models.IntegerField()
    entered_by_user = models.TextField()
    date_entered = models.TextField()
    user_ip_address = models.TextField()

    class Meta:
        managed = False  
        db_table = 'announced_state_results'


class AnnouncedWardResults(models.Model):
    result_id = models.AutoField(primary_key=True)
    ward_name = models.TextField()
    party_abbreviation = models.TextField()
    party_score = models.IntegerField()
    entered_by_user = models.TextField()
    date_entered = models.TextField()
    user_ip_address = models.TextField()

    class Meta:
        managed = False  
        db_table = 'announced_ward_results'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

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
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

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
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

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


class Lga(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    lga_id = models.IntegerField()
    lga_name = models.TextField()
    state_id = models.IntegerField()
    lga_description = models.TextField(blank=True, null=True)
    entered_by_user = models.TextField()
    date_entered = models.TextField()
    user_ip_address = models.TextField()

    class Meta:
        managed = False  
        db_table = 'lga'


class Party(models.Model):
    partyid = models.TextField()
    partyname = models.TextField()

    class Meta:
        managed = False  
        db_table = 'party'


class PollingUnit(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    polling_unit_id = models.IntegerField()
    ward_id = models.IntegerField()
    lga_id = models.IntegerField()
    uniquewardid = models.IntegerField(blank=True, null=True)
    polling_unit_number = models.TextField(blank=True, null=True)
    polling_unit_name = models.TextField(blank=True, null=True)
    polling_unit_description = models.TextField(blank=True, null=True)
    lat = models.TextField(blank=True, null=True)
    long = models.TextField(blank=True, null=True)
    entered_by_user = models.TextField(blank=True, null=True)
    date_entered = models.TextField(blank=True, null=True)
    user_ip_address = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  
        db_table = 'polling_unit'


class States(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_name = models.TextField()

    class Meta:
        managed = False  
        db_table = 'states'


class Ward(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    ward_id = models.IntegerField()
    ward_name = models.TextField()
    lga_id = models.IntegerField()
    ward_description = models.TextField(blank=True, null=True)
    entered_by_user = models.TextField()
    date_entered = models.TextField()
    user_ip_address = models.TextField()

    class Meta:
        managed = False  
        db_table = 'ward'
