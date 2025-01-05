"""
URL configuration for EventApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from EventApp.Models.viewsets import (
    AddressViewSet, ArtistsViewSet, AuthGroupViewSet,
    AuthGroupPermissionsViewSet, AuthPermissionViewSet, AuthUserViewSet,
    AuthUserGroupsViewSet, AuthUserUserPermissionsViewSet, BandsViewSet,
    ConcertsViewSet, ContactInfoViewSet, ContributionTypesViewSet,
    ContributionsViewSet, DjangoAdminLogViewSet, DjangoContentTypeViewSet,
    DjangoMigrationsViewSet, DjangoSessionViewSet, EmployeesViewSet,
    EventSeriesViewSet, LocalizationsViewSet, MembershipsViewSet,
    ParticipantsViewSet, PartnersViewSet, PerformersViewSet,
    PersonsViewSet, RolesViewSet, StylesViewSet, TicketTypesViewSet,
    TicketsViewSet, WorksViewSet
)

router = DefaultRouter()
router.register(r'addresses', AddressViewSet)
router.register(r'artists', ArtistsViewSet)
router.register(r'auth_groups', AuthGroupViewSet)
router.register(r'auth_group_permissions', AuthGroupPermissionsViewSet)
router.register(r'auth_permissions', AuthPermissionViewSet)
router.register(r'auth_users', AuthUserViewSet)
router.register(r'auth_user_groups', AuthUserGroupsViewSet)
router.register(r'auth_user_user_permissions', AuthUserUserPermissionsViewSet)
router.register(r'bands', BandsViewSet)
router.register(r'concerts', ConcertsViewSet)
router.register(r'contact_info', ContactInfoViewSet)
router.register(r'contribution_types', ContributionTypesViewSet)
router.register(r'contributions', ContributionsViewSet)
router.register(r'django_admin_log', DjangoAdminLogViewSet)
router.register(r'django_content_type', DjangoContentTypeViewSet)
router.register(r'django_migrations', DjangoMigrationsViewSet)
router.register(r'django_session', DjangoSessionViewSet)
router.register(r'employees', EmployeesViewSet)
router.register(r'event_series', EventSeriesViewSet)
router.register(r'localizations', LocalizationsViewSet)
router.register(r'memberships', MembershipsViewSet)
router.register(r'participants', ParticipantsViewSet)
router.register(r'partners', PartnersViewSet)
router.register(r'performers', PerformersViewSet)
router.register(r'persons', PersonsViewSet)
router.register(r'roles', RolesViewSet)
router.register(r'styles', StylesViewSet)
router.register(r'ticket_types', TicketTypesViewSet)
router.register(r'tickets', TicketsViewSet)
router.register(r'works', WorksViewSet)

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Music App API",
      default_version='v1',
      description="API for music events, concerts, and artists",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@musicapp.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('openapi/', include(router.urls)),
    path('swagger/', schema_view.as_view(), name='swagger-docs'),

]

