from rest_framework import viewsets
from OCR_P12.permissions import PermissionEvent, ActualDjangoModelPermissions
from events.models import Event
from events.serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    permission_classes = [PermissionEvent, ActualDjangoModelPermissions]
    serializer_class = EventSerializer

    def get_queryset(self):
        if 'Management' in self.request.user.groups.all().values_list("name", flat=True):
            return Event.objects.all()

        elif 'Sales' in self.request.user.groups.all().values_list("name", flat=True):
            return Event.objects.all()

        elif 'Support' in self.request.user.groups.all().values_list("name", flat=True):
            return Event.objects.all()
