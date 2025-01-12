from datetime import datetime

from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from django.db import connection
from .models import (Address, Artists, AuthGroup, AuthGroupPermissions, AuthPermission, AuthUser, AuthUserGroups, AuthUserUserPermissions, Bands, Concerts, ContactInfo, ContributionTypes, Contributions, DjangoAdminLog, DjangoContentType, DjangoMigrations, DjangoSession, Employees, EventSeries, Localizations, Memberships, Participants, Partners, Performers, Persons, Roles, Styles, TicketTypes, Tickets, Works, ConcertDetailsView, EmployeeWorkDetails, TicketSalesSummary)
from .serializers import AddressSerializer, ArtistsSerializer, AuthGroupSerializer, AuthGroupPermissionsSerializer, AuthPermissionSerializer, AuthUserSerializer, AuthUserGroupsSerializer, AuthUserUserPermissionsSerializer, BandsSerializer, ConcertsSerializer, ContactInfoSerializer, ContributionTypesSerializer, ContributionsSerializer, DjangoAdminLogSerializer, DjangoContentTypeSerializer, DjangoMigrationsSerializer, DjangoSessionSerializer, EmployeesSerializer, EventSeriesSerializer, LocalizationsSerializer, MembershipsSerializer, ParticipantsSerializer, PartnersSerializer, PerformersSerializer, PersonsSerializer, RolesSerializer, StylesSerializer, TicketTypesSerializer, TicketsSerializer, WorksSerializer,ConcertDetailsViewSerializer,EmployeeWorkDetailsSerializer,TicketSalesSummarySerializer


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

class ConcertDetailsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ConcertDetailsView.objects.all()
    serializer_class = ConcertDetailsViewSerializer


class EmployeeWorkDetailsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EmployeeWorkDetails.objects.all()
    serializer_class = EmployeeWorkDetailsSerializer


class TicketSalesSummaryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TicketSalesSummary.objects.all()
    serializer_class = TicketSalesSummarySerializer
    @action(detail=False, methods=['get'], url_path=r'summary_by_series/(?P<series_id>\d+)')
    def summary_by_series(self, request, series_id=None):
        queryset = TicketSalesSummary.objects.filter(series_id=series_id)
        serializer = self.get_serializer(queryset, many=True)
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

    @action(detail=False, methods=['post'], url_path='delete-band-performances')
    def delete_band_performances(self, request):
        """
        Endpoint to call DeleteBandPerformancesAndAdjustPlaces procedure
        """
        band_id = request.data.get('band_id')
        concert_id = request.data.get('concert_id')

        if not (band_id and concert_id):
            return Response(
                {"error": "band_id and concert_id are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        with connection.cursor() as cursor:
            cursor.callproc("DeleteBandPerformancesAndAdjustPlaces", [band_id, concert_id])

        return Response({"message": "Band performances deleted and places adjusted"}, status=status.HTTP_200_OK)

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

    @action(detail=False, methods=['post'], url_path='mark-used-tickets')
    def mark_used_tickets(self, request):
        """
        Endpoint to call MarkUsedTicketsForPastConcerts procedure
        """
        with connection.cursor() as cursor:
            cursor.callproc("MarkUsedTicketsForPastConcerts")
        return Response({"message": "Procedure executed successfully"}, status=status.HTTP_200_OK)


class WorksViewSet(viewsets.ModelViewSet):
    queryset = Works.objects.all()
    serializer_class = WorksSerializer

    @action(detail=False, methods=['post'], url_path='update-salaries')
    def update_salaries(self, request):
        """
        Endpoint to call UpdateSalariesByWorkRoleAndConcert procedure
        """
        concert_id = request.data.get('concert_id')
        work_role_id = request.data.get('work_role_id')
        multiplier = request.data.get('multiplier')

        if not (concert_id and work_role_id and multiplier):
            return Response(
                {"error": "concert_id, work_role_id, and multiplier are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        with connection.cursor() as cursor:
            cursor.callproc("UpdateSalariesByWorkRoleAndConcert", [concert_id, work_role_id, multiplier])

        return Response({"message": "Salaries updated successfully"}, status=status.HTTP_200_OK)
