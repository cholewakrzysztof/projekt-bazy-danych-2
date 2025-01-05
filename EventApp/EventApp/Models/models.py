# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=40, blank=True, null=True)
    province = models.CharField(max_length=40, blank=True, null=True)
    post_code = models.CharField(max_length=40, blank=True, null=True)
    city = models.CharField(max_length=40, blank=True, null=True)
    street = models.CharField(max_length=40, blank=True, null=True)
    street_number = models.CharField(max_length=4, blank=True, null=True)
    apartment_number = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'address'


class Artists(models.Model):
    artist_id = models.AutoField(primary_key=True)
    person_id = models.IntegerField(blank=True, null=True)
    pseudonym = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'artists'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Bands(models.Model):
    band_id = models.AutoField(primary_key=True)
    band_name = models.CharField(max_length=60, blank=True, null=True)
    address_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bands'


class Concerts(models.Model):
    concert_id = models.AutoField(primary_key=True)
    localization_id = models.IntegerField(blank=True, null=True)
    event_series_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=60, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    duration = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'concerts'


class ContactInfo(models.Model):
    contact_info_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact_info'


class ContributionTypes(models.Model):
    contribution_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contribution_types'


class Contributions(models.Model):
    contribution_id = models.AutoField(primary_key=True)
    partner_id = models.IntegerField(blank=True, null=True)
    series_id = models.IntegerField(blank=True, null=True)
    contribution_type_id = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contributions'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

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
    id = models.BigAutoField(primary_key=True)
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


class Employees(models.Model):
    employee_id = models.AutoField(primary_key=True)
    person_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'


class EventSeries(models.Model):
    series_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_series'


class Localizations(models.Model):
    localization_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, blank=True, null=True)
    address_id = models.IntegerField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'localizations'


class Memberships(models.Model):
    membership_id = models.AutoField(primary_key=True)
    artist_id = models.IntegerField(blank=True, null=True)
    band_id = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    position = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'memberships'


class Participants(models.Model):
    participant_id = models.AutoField(primary_key=True)
    person_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'participants'


class Partners(models.Model):
    partner_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, blank=True, null=True)
    tin = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partners'


class Performers(models.Model):
    perform_id = models.AutoField(primary_key=True)
    concert_id = models.IntegerField(blank=True, null=True)
    band_id = models.IntegerField(blank=True, null=True)
    style_id = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    place_in_concert = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'performers'


class Persons(models.Model):
    person_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=40, blank=True, null=True)
    last_name = models.CharField(max_length=40, blank=True, null=True)
    sex = models.TextField(blank=True, null=True)  # This field type is a guess.
    age = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persons'


class Roles(models.Model):
    role_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class Styles(models.Model):
    style_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'styles'


class TicketTypes(models.Model):
    type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ticket_types'


class Tickets(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    concert_id = models.IntegerField(blank=True, null=True)
    price = models.IntegerField()
    type_id = models.IntegerField(blank=True, null=True)
    participant_id = models.IntegerField(blank=True, null=True)
    place = models.CharField(max_length=60, blank=True, null=True)
    used = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tickets'


class Works(models.Model):
    work_id = models.AutoField(primary_key=True)
    concert_id = models.IntegerField(blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)
    employee_id = models.IntegerField(blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    work_hours = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'works'


