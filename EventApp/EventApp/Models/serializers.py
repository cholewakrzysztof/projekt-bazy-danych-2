from rest_framework import serializers
from .models import Address, Artists, AuthGroup, AuthGroupPermissions, AuthPermission, AuthUser, AuthUserGroups, AuthUserUserPermissions, Bands, Concerts, ContactInfo, ContributionTypes, Contributions, DjangoAdminLog, DjangoContentType, DjangoMigrations, DjangoSession, Employees, EventSeries, Localizations, Memberships, Participants, Partners, Performers, Persons, Roles, Styles, TicketTypes, Tickets, Works

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class ArtistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artists
        fields = '__all__'

class AuthGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthGroup
        fields = '__all__'

class AuthGroupPermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthGroupPermissions
        fields = '__all__'

class AuthPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthPermission
        fields = '__all__'

class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = '__all__'

class AuthUserGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUserGroups
        fields = '__all__'

class AuthUserUserPermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUserUserPermissions
        fields = '__all__'

class BandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bands
        fields = '__all__'

class ConcertsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concerts
        fields = '__all__'

class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'

class ContributionTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContributionTypes
        fields = '__all__'

class ContributionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributions
        fields = '__all__'

class DjangoAdminLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoAdminLog
        fields = '__all__'

class DjangoContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoContentType
        fields = '__all__'

class DjangoMigrationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoMigrations
        fields = '__all__'

class DjangoSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoSession
        fields = '__all__'

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'

class EventSeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventSeries
        fields = '__all__'

class LocalizationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localizations
        fields = '__all__'

class MembershipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memberships
        fields = '__all__'

class ParticipantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participants
        fields = '__all__'

class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = '__all__'

class PerformersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performers
        fields = '__all__'

class PersonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persons
        fields = '__all__'

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'

class StylesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Styles
        fields = '__all__'

class TicketTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketTypes
        fields = '__all__'

class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = '__all__'

class WorksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Works
        fields = '__all__'
