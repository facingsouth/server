from events.models import Event, Follower
from rest_framework import serializers

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'location_lon', 'location_lat',
                  'started_on', 'creator', 'group_size', )

class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ('follower', 'event', 'followed_on', )
