from rest_framework import serializers
from main_app.models import Service

class ServiceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    
    def create(self, validated_data):
        """
        Create and return a new 'service' instance, given the validated data.
        """
        return Service.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update and return and existing 'Service' instance, given the validated data
        """
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance
    