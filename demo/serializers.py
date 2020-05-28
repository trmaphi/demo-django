from rest_framework import serializers
from .models import People, Planet


class PeopleSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=255)
    homeworld = serializers.PrimaryKeyRelatedField(
        queryset=Planet.objects.all())
    height = serializers.IntegerField()
    mass = serializers.IntegerField()
    hair_color = serializers.ChoiceField(choices=People.HAIR_COLOR_CHOICES)
    created = serializers.DateTimeField()

    class Meta:
        model = People

    # Create from validate data
    def create(self, validated_data):
        return People.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.title)
        instance.homeworld = validated_data.get('homeworld', instance.code)
        instance.height = validated_data.get('height', instance.linenos)
        instance.mass = validated_data.get('mass', instance.language)
        instance.hair_color = validated_data.get('hair_color', instance.style)
        instance.save()
        return instance

class PlanetSerializer(serializers.Serializer):

    class Meta:
        model = Planet


    # Create from validate data
    def create(self, validated_data):
        return People.objects.create(**validated_data)
