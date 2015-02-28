from django.forms import widgets
from rest_framework import serializers
from gps.models import GpsNode, GpsNodeMetrics


class GpsNodeSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    ident = serializers.CharField(required=True, allow_blank=False)

    def create(self, validated_data):
        """
        Create and return a new `GpsNode` instance, given the validated data.
        """
        return GpsNode.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.ident = validated_data.get('ident', instance.ident)
        instance.save()
        return instance
