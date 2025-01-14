from datetime import datetime, timedelta

from django.apps import apps
from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view

from .models import (Address, Artists, AuthGroup, AuthGroupPermissions, AuthPermission, AuthUser, AuthUserGroups,
                     AuthUserUserPermissions, Bands, Concerts, ContactInfo, ContributionTypes, Contributions,
                     DjangoAdminLog, DjangoContentType, DjangoMigrations, DjangoSession, Employees, EventSeries,
                     Localizations, Memberships, Participants, Partners, Performers, Persons, Roles, Styles,
                     TicketTypes, Tickets, Works, Users)
from .serializers import AddressSerializer, ArtistsSerializer, AuthGroupSerializer, AuthGroupPermissionsSerializer, \
    AuthPermissionSerializer, AuthUserSerializer, AuthUserGroupsSerializer, AuthUserUserPermissionsSerializer, \
    BandsSerializer, ConcertsSerializer, ContactInfoSerializer, ContributionTypesSerializer, ContributionsSerializer, \
    DjangoAdminLogSerializer, DjangoContentTypeSerializer, DjangoMigrationsSerializer, DjangoSessionSerializer, \
    EmployeesSerializer, EventSeriesSerializer, LocalizationsSerializer, MembershipsSerializer, ParticipantsSerializer, \
    PartnersSerializer, PerformersSerializer, PersonsSerializer, RolesSerializer, StylesSerializer, \
    TicketTypesSerializer, TicketsSerializer, WorksSerializer, UsersSerializer, \
    OperationRequestSerializer
from ..LoginComponent.LoggedUserContext import LoggedUserContext
from django.db import connection, IntegrityError
from .models import (Address, Artists, AuthGroup, AuthGroupPermissions, AuthPermission, AuthUser, AuthUserGroups, AuthUserUserPermissions, Bands, Concerts, ContactInfo, ContributionTypes, Contributions, DjangoAdminLog, DjangoContentType, DjangoMigrations, DjangoSession, Employees, EventSeries, Localizations, Memberships, Participants, Partners, Performers, Persons, Roles, Styles, TicketTypes, Tickets, Works, ConcertDetailsView, EmployeeWorkDetails, TicketSalesSummary)
from .serializers import AddressSerializer, ArtistsSerializer, AuthGroupSerializer, AuthGroupPermissionsSerializer, AuthPermissionSerializer, AuthUserSerializer, AuthUserGroupsSerializer, AuthUserUserPermissionsSerializer, BandsSerializer, ConcertsSerializer, ContactInfoSerializer, ContributionTypesSerializer, ContributionsSerializer, DjangoAdminLogSerializer, DjangoContentTypeSerializer, DjangoMigrationsSerializer, DjangoSessionSerializer, EmployeesSerializer, EventSeriesSerializer, LocalizationsSerializer, MembershipsSerializer, ParticipantsSerializer, PartnersSerializer, PerformersSerializer, PersonsSerializer, RolesSerializer, StylesSerializer, TicketTypesSerializer, TicketsSerializer, WorksSerializer,ConcertDetailsViewSerializer,EmployeeWorkDetailsSerializer,TicketSalesSummarySerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.using(LoggedUserContext.get_connection_string()).all()
    serializer_class = AddressSerializer


class ArtistsViewSet(viewsets.ModelViewSet):
    queryset = Artists.objects.using(LoggedUserContext.get_connection_string()).all()
    serializer_class = ArtistsSerializer


class AuthGroupViewSet(viewsets.ModelViewSet):
    queryset = AuthGroup.objects.using(LoggedUserContext.get_connection_string()).all()
    serializer_class = AuthGroupSerializer


class AuthGroupPermissionsViewSet(viewsets.ModelViewSet):
    queryset = AuthGroupPermissions.objects.using(LoggedUserContext.get_connection_string()).all()
    serializer_class = AuthGroupPermissionsSerializer


class AuthPermissionViewSet(viewsets.ModelViewSet):
    queryset = AuthPermission.objects.using(LoggedUserContext.get_connection_string()).all()
    serializer_class = AuthPermissionSerializer


class AuthUserViewSet(viewsets.ModelViewSet):
    queryset = AuthUser.objects.using(LoggedUserContext.get_connection_string()).all()
    serializer_class = AuthUserSerializer


class AuthUserGroupsViewSet(viewsets.ModelViewSet):
    queryset = AuthUserGroups.objects.using(LoggedUserContext.get_connection_string()).all()
    serializer_class = AuthUserGroupsSerializer


class AuthUserUserPermissionsViewSet(viewsets.ModelViewSet):
    queryset = AuthUserUserPermissions.objects.using(LoggedUserContext.get_connection_string()).all()
    serializer_class = AuthUserUserPermissionsSerializer


class BandsViewSet(viewsets.ModelViewSet):
    queryset = Bands.objects.using(LoggedUserContext.get_connection_string()).all()
    serializer_class = BandsSerializer


class ConcertsViewSet(viewsets.ModelViewSet):
    queryset = Concerts.objects.all()
    serializer_class = ConcertsSerializer

    @action(
        detail=False,
        methods=['get'],
        url_path=r'filter/(?P<localization_id>\d+|null)/(?P<date>[^/]+|null)/(?P<start_date>[^/]+|null)/(?P<end_date>[^/]+|null)',
        permission_classes=[AllowAny],
    )
    def filter_concerts(self, request, localization_id=None, date=None, start_date=None, end_date=None):
        """
        Endpoint dla filtrowania koncertów i zespołów:
        - localization_id: ID lokalizacji (int lub null)
        - date: Data koncertu (string w formacie YYYY-MM-DD lub null)
        - start_date: Początek zakresu dat (string w formacie YYYY-MM-DD lub null)
        - end_date: Koniec zakresu dat (string w formacie YYYY-MM-DD lub null)
        """

        # Zamiana "null" na None dla parametrów opcjonalnych
        localization_id = None if localization_id == "null" else localization_id
        date = None if date == "null" else date
        start_date = None if start_date == "null" else start_date
        end_date = None if end_date == "null" else end_date

        # Filtruj koncerty według lokalizacji i daty
        concert_query = Q()
        if localization_id:
            concert_query &= Q(localization_id=localization_id)
        if date:
            concert_query &= Q(date=date)

        concerts = Concerts.objects.filter(concert_query)

        # Filtruj zespoły według zakresu dat
        band_query = Q()
        if start_date and end_date:
            band_query &= Q(start_date__lte=end_date) & Q(end_date__gte=start_date)

        memberships = Memberships.objects.filter(band_query)
        if not start_date or not end_date:
            # Jeśli brakuje start_date lub end_date, wybierz wszystkie zespoły z powiązaniami
            memberships = Memberships.objects.all()

        bands = Bands.objects.filter(band_id__in=memberships.values_list('band_id', flat=True))

        # Serializacja wyników
        concert_data = ConcertsSerializer(concerts, many=True).data
        band_data = BandsSerializer(bands, many=True).data

        # Przygotowanie odpowiedzi
        response_data = {
            "concerts": concert_data,
            "bands": band_data,
        }

        return Response(response_data, status=status.HTTP_200_OK)

class ContactInfoViewSet(viewsets.ModelViewSet):
    queryset = ContactInfo.objects.using(LoggedUserContext.get_connection_string()).all()
    serializer_class = ContactInfoSerializer


class ContributionTypesViewSet(viewsets.ModelViewSet):
    queryset = ContributionTypes.objects.using(LoggedUserContext.get_connection_string()).all()
    serializer_class = ContributionTypesSerializer


class ContributionsViewSet(viewsets.ModelViewSet):
    queryset = Contributions.objects.using(LoggedUserContext.get_connection_string()).all()
    serializer_class = ContributionsSerializer


class DjangoAdminLogViewSet(viewsets.ModelViewSet):
    queryset = DjangoAdminLog.objects.using(LoggedUserContext.get_connection_string()).all()
    serializer_class = DjangoAdminLogSerializer


class DjangoContentTypeViewSet(viewsets.ModelViewSet):
    queryset = DjangoContentType.objects.using(LoggedUserContext.get_connection_string()).all()
    serializer_class = DjangoContentTypeSerializer


class DjangoMigrationsViewSet(viewsets.ModelViewSet):
    queryset = DjangoMigrations.objects.using(LoggedUserContext.get_connection_string()).all()
    serializer_class = DjangoMigrationsSerializer


class DjangoSessionViewSet(viewsets.ModelViewSet):
    queryset = DjangoSession.objects.using(LoggedUserContext.get_connection_string()).all()
    serializer_class = DjangoSessionSerializer


class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.using(LoggedUserContext.get_connection_string()).all()
    serializer_class = EmployeesSerializer


class EventSeriesViewSet(viewsets.ModelViewSet):
    queryset = EventSeries.objects.using(LoggedUserContext.get_connection_string()).all()
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

    queryset = Tickets.objects.all()
    serializer_class = TicketsSerializer

    @action(detail=False, methods=['post'], url_path='purchase-ticket')
    def purchase_ticket(self, request):
        """
        Endpoint do zakupu biletu.
        """
        concert_id = request.data.get('concert_id')
        ticket_type = request.data.get('ticket_type')
        participant_id = request.data.get('participant_id')

        if not (concert_id and ticket_type and participant_id):
            return Response(
                {"error": "concert_id, ticket_type, and participant_id are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Pobierz pierwszy dostępny bilet dla danego koncertu i typu
        ticket = Tickets.objects.filter(
            concert_id=concert_id,
            type_id=ticket_type,
            participant_id__isnull=True
        ).first()

        if not ticket:
            return Response(
                {"error": "No available tickets of the selected type for this concert."},
                status=status.HTTP_404_NOT_FOUND
            )

        # Zaktualizuj dane biletu
        ticket.participant_id = participant_id
        ticket.save()

        return Response(TicketsSerializer(ticket).data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='sold-tickets/(?P<concert_id>\d+)')
    def sold_tickets(self, request, concert_id=None):
        """
        Endpoint do sprawdzania sprzedanych biletów na dany koncert.
        """
        tickets = Tickets.objects.filter(concert_id=concert_id, participant_id__isnull=False)

        if not tickets.exists():
            return Response(
                {"message": "No sold tickets found for this concert."},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(TicketsSerializer(tickets, many=True).data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], url_path='use-ticket')
    def use_ticket(self, request):
        """
        Endpoint do oznaczania biletu jako wykorzystanego.
        """
        ticket_id = request.data.get('ticket_id')

        if not ticket_id:
            return Response(
                {"error": "ticket_id is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        ticket = Tickets.objects.filter(ticket_id=ticket_id, used=False).first()

        if not ticket:
            return Response(
                {"error": "Ticket not found or already used."},
                status=status.HTTP_404_NOT_FOUND
            )

        # Oznacz bilet jako wykorzystany
        ticket.used = True
        ticket.save()

        return Response(
            {"message": "Ticket marked as used.", "ticket": TicketsSerializer(ticket).data},
            status=status.HTTP_200_OK
        )


class LocalizationsViewSet(viewsets.ModelViewSet):
    queryset = Localizations.objects.using(LoggedUserContext.get_connection_string()).all()
    serializer_class = LocalizationsSerializer


class MembershipsViewSet(viewsets.ModelViewSet):
    queryset = Memberships.objects.using(LoggedUserContext.get_connection_string()).all()
    serializer_class = MembershipsSerializer


class ParticipantsViewSet(viewsets.ModelViewSet):
    queryset = Participants.objects.using(LoggedUserContext.get_connection_string()).all()
    serializer_class = ParticipantsSerializer


class PartnersViewSet(viewsets.ModelViewSet):
    queryset = Partners.objects.using(LoggedUserContext.get_connection_string()).all()
    serializer_class = PartnersSerializer


class PerformersViewSet(viewsets.ModelViewSet):
    queryset = Performers.objects.using(LoggedUserContext.get_connection_string()).all()
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
    queryset = Persons.objects.using(LoggedUserContext.get_connection_string()).all()
    serializer_class = PersonsSerializer


class RolesViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.using(LoggedUserContext.get_connection_string()).all()
    serializer_class = RolesSerializer


class StylesViewSet(viewsets.ModelViewSet):
    queryset = Styles.objects.using(LoggedUserContext.get_connection_string()).all()
    serializer_class = StylesSerializer


class TicketTypesViewSet(viewsets.ModelViewSet):
    queryset = TicketTypes.objects.using(LoggedUserContext.get_connection_string()).all()
    serializer_class = TicketTypesSerializer


class TicketsViewSet(viewsets.ModelViewSet):
    queryset = Tickets.objects.using(LoggedUserContext.get_connection_string()).all()
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
    queryset = Works.objects.using(LoggedUserContext.get_connection_string()).all()
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


class UsersViewSet(viewsets.ViewSet):
    queryset = Users.objects.using(LoggedUserContext.get_connection_string()).all()
    serializer_class = UsersSerializer

    @action(detail=False, methods=['get'], url_path=r'login/(?P<login>.+)/(?P<password>.+)')
    def login_user(self, request, login=None, password=None):
        sql = "SELECT * FROM users WHERE login = '{}' AND password = '{}'".format(login, password)
        response = Users.objects.using('default').raw(sql)

        if len(response) > 0:
            user = Users.objects.using('default').get(login=login, password=password)
            user.session_expires = datetime.now() + timedelta(minutes=5)
            user.save()

            LoggedUserContext.setup_logged_context(user.session_expires, user.user_type)

            serializer = UsersSerializer(user, many=False)
            return Response(serializer.data)

        return Response([])

    @action(detail=False, methods=['get'], url_path=r'all')
    def get_all(self, request):
        response = Users.objects.using('default').all()
        serializer = UsersSerializer(response, many=True)
        return Response(serializer.data)

class PerformOperationViewSet(viewsets.ViewSet):
    serializer_class = OperationRequestSerializer

    @swagger_auto_schema(request_body=OperationRequestSerializer)
    @action(detail=False, methods=['post'], url_path=r'')
    def perform_operation(self, request):
        serializer = OperationRequestSerializer(data=request.data)

        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']
            database_name = serializer.validated_data['database_name']
            operation_type = serializer.validated_data['operation_type']

            user = Users.objects.using('default').get(user_id=user_id)
            user_type = UsersSerializer(user, many=False).data['user_type']

            result = self.execute_operation(database_name, operation_type, user_type)
            message = (f"Operation '{operation_type}' "
                       f"performed for user {user_id} (type: {user_type}) "
                       f"on database '{database_name}', "
                       f"result: {result}")

            return Response({"message": message})

        return Response(serializer.errors, status=400)

    @staticmethod
    def create_model(model,conn):
        try:
            instance = model.objects.using(conn).create()
            return f"Created a new {model.__name__} instance"
        except IntegrityError as e:
            return f"Error creating {model.__name__}: {str(e)}"

    @staticmethod
    def read(model,conn):
        instances = model.objects.using(conn).all()
        return f"Read operation on {model.__name__} model, found {len(instances)} instances"

    @staticmethod
    def update_model(model,conn):
        instance = model.objects.using(conn).first()
        if instance:
            instance.save()
            return f"Updated {model.__name__} instance"
        return f"No {model.__name__} instance to update"

    @staticmethod
    def delete(model,conn):
        try:
            instance = model.objects.using(conn).first()
            if instance:
                instance.delete()
                return f"Deleted {model.__name__} instance"
            return f"No {model.__name__} instance to delete"
        except IntegrityError as e:
            return f"Error deleting {model.__name__}: {str(e)}"

    operation_map = {
        'CREATE': create_model,
        'READ': read,
        'UPDATE': update_model,
        'DELETE': delete
    }

    def execute_operation(self, database_name, operation_type, conn):
        try:
            model = apps.get_model('EventApp', database_name)
        except LookupError:
            return 'Model not found for database name'


        operation_func = self.operation_map.get(operation_type)

        if operation_func:
            return operation_func(model,conn)
        else:
            return 'Invalid operation'