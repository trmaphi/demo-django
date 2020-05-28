import json

from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from .models import People, Planet
from .serializers import PeopleSerializer, PlanetSerializer


class PlanetModelViewSet(viewsets.ModelViewSet):

    serializer_class = PlanetSerializer
    queryset = Planet.objects.all()

    def list(self, request):
        serializer = PlanetSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        planet = get_object_or_404(self.queryset, pk=pk)
        serializer = PlanetSerializer(planet)
        return Response(serializer.data)


class PeopleModelViewSet(viewsets.ModelViewSet):

    serializer_class = PeopleSerializer
    queryset = People.objects.all()

    def list(self, request):
        serializer = PeopleSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        people = get_object_or_404(self.queryset, pk=pk)
        serializer = PeopleSerializer(people)
        return Response(serializer.data)

    def create(self, request):
        serializer = PeopleModelSerializer(data=request.data)
        if serializer.is_valid():
            People.objects.create(
                name=serializer.validated_data['name'],
                homeworld=serializer.validated_data['homeworld'],
                height=serializer.validated_data['height'],
                mass=serializer.validated_data['mass'],
                hair_color=serializer.validated_data['hair_color'])
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

