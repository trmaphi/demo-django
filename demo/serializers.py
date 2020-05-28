from rest_framework import serializers
from .models import People, Planet


class PeopleSerializer(serializers.Serializer):

    # Apply to all object
    name = serializers.CharField(max_length=255)
    homeworld = serializers.PrimaryKeyRelatedField(
        queryset=Planet.objects.all())
    height = serializers.IntegerField()
    mass = serializers.IntegerField()
    hair_color = serializers.ChoiceField(choices=People.HAIR_COLOR_CHOICES)
    created = serializers.DateTimeField()

    class Meta:
        model = People

    # Validated data will be used to create object
    def create(self, validated_data):
        return People.objects.create(**validated_data)

class PlanetSerializer(serializers.Serializer):

    class Meta:
        model = Planet


    # Validated data will be used to create object
    def create(self, validated_data):
        return People.objects.create(**validated_data)
