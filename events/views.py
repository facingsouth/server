from rest_framework import viewsets
from events.models import Event, Follower
from events.serializers import EventSerializer, FollowerSerializer


class EventViewSet(viewsets.ModelViewSet):
    """API endpoint for listing and creating events."""
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class FollowerViewSet(viewsets.ModelViewSet):
    """API endpoint for listing and creating followers."""
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
