from datetime import datetime

from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action

from .models import (Address, Artists, AuthGroup, AuthGroupPermissions, AuthPermission, AuthUser, AuthUserGroups, AuthUserUserPermissions, Bands, Concerts, ContactInfo, ContributionTypes, Contributions, DjangoAdminLog, DjangoContentType, DjangoMigrations, DjangoSession, Employees, EventSeries, Localizations, Memberships, Participants, Partners, Performers, Persons, Roles, Styles, TicketTypes, Tickets, Works)
from .serializers import AddressSerializer, ArtistsSerializer, AuthGroupSerializer, AuthGroupPermissionsSerializer, AuthPermissionSerializer, AuthUserSerializer, AuthUserGroupsSerializer, AuthUserUserPermissionsSerializer, BandsSerializer, ConcertsSerializer, ContactInfoSerializer, ContributionTypesSerializer, ContributionsSerializer, DjangoAdminLogSerializer, DjangoContentTypeSerializer, DjangoMigrationsSerializer, DjangoSessionSerializer, EmployeesSerializer, EventSeriesSerializer, LocalizationsSerializer, MembershipsSerializer, ParticipantsSerializer, PartnersSerializer, PerformersSerializer, PersonsSerializer, RolesSerializer, StylesSerializer, TicketTypesSerializer, TicketsSerializer, WorksSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class ArtistsViewSet(viewsets.ModelViewSet):
    queryset = Artists.objects.all()
    serializer_class = ArtistsSerializer


class AuthGroupViewSet(viewsets.ModelViewSet):
    queryset = AuthGroup.objects.all()
    serializer_class = AuthGroupSerializer


class AuthGroupPermissionsViewSet(viewsets.ModelViewSet):
    queryset = AuthGroupPermissions.objects.all()
    serializer_class = AuthGroupPermissionsSerializer


class AuthPermissionViewSet(viewsets.ModelViewSet):
    queryset = AuthPermission.objects.all()
    serializer_class = AuthPermissionSerializer


class AuthUserViewSet(viewsets.ModelViewSet):
    queryset = AuthUser.objects.all()
    serializer_class = AuthUserSerializer


class AuthUserGroupsViewSet(viewsets.ModelViewSet):
    queryset = AuthUserGroups.objects.all()
    serializer_class = AuthUserGroupsSerializer


class AuthUserUserPermissionsViewSet(viewsets.ModelViewSet):
    queryset = AuthUserUserPermissions.objects.all()
    serializer_class = AuthUserUserPermissionsSerializer


class BandsViewSet(viewsets.ModelViewSet):
    queryset = Bands.objects.all()
    serializer_class = BandsSerializer


class ConcertsViewSet(viewsets.ModelViewSet):
    queryset = Concerts.objects.all()
    serializer_class = ConcertsSerializer


class ContactInfoViewSet(viewsets.ModelViewSet):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer


class ContributionTypesViewSet(viewsets.ModelViewSet):
    queryset = ContributionTypes.objects.all()
    serializer_class = ContributionTypesSerializer


class ContributionsViewSet(viewsets.ModelViewSet):
    queryset = Contributions.objects.all()
    serializer_class = ContributionsSerializer


class DjangoAdminLogViewSet(viewsets.ModelViewSet):
    queryset = DjangoAdminLog.objects.all()
    serializer_class = DjangoAdminLogSerializer


class DjangoContentTypeViewSet(viewsets.ModelViewSet):
    queryset = DjangoContentType.objects.all()
    serializer_class = DjangoContentTypeSerializer


class DjangoMigrationsViewSet(viewsets.ModelViewSet):
    queryset = DjangoMigrations.objects.all()
    serializer_class = DjangoMigrationsSerializer


class DjangoSessionViewSet(viewsets.ModelViewSet):
    queryset = DjangoSession.objects.all()
    serializer_class = DjangoSessionSerializer


class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer


class EventSeriesViewSet(viewsets.ModelViewSet):
    queryset = EventSeries.objects.all()
    serializer_class = EventSeriesSerializer

    @action(detail=False, methods=['get'], url_path=r'custom_action/(?P<id>.+)')
    def events_before_date(self, request, id=None):
        queryset = EventSeries.objects.filter(series_id__exact=id)

        serializer = EventSeriesSerializer(queryset, many=True)
        return Response(serializer.data)


class LocalizationsViewSet(viewsets.ModelViewSet):
    queryset = Localizations.objects.all()
    serializer_class = LocalizationsSerializer


class MembershipsViewSet(viewsets.ModelViewSet):
    queryset = Memberships.objects.all()
    serializer_class = MembershipsSerializer


class ParticipantsViewSet(viewsets.ModelViewSet):
    queryset = Participants.objects.all()
    serializer_class = ParticipantsSerializer


class PartnersViewSet(viewsets.ModelViewSet):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer


class PerformersViewSet(viewsets.ModelViewSet):
    queryset = Performers.objects.all()
    serializer_class = PerformersSerializer


class PersonsViewSet(viewsets.ModelViewSet):
    queryset = Persons.objects.all()
    serializer_class = PersonsSerializer


class RolesViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer


class StylesViewSet(viewsets.ModelViewSet):
    queryset = Styles.objects.all()
    serializer_class = StylesSerializer


class TicketTypesViewSet(viewsets.ModelViewSet):
    queryset = TicketTypes.objects.all()
    serializer_class = TicketTypesSerializer


class TicketsViewSet(viewsets.ModelViewSet):
    queryset = Tickets.objects.all()
    serializer_class = TicketsSerializer


class WorksViewSet(viewsets.ModelViewSet):
    queryset = Works.objects.all()
    serializer_class = WorksSerializer
