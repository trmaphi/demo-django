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
    # Public
    # permission_classes

    def list(self, request):
        serializer = PlanetSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        planet = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = PlanetSerializer(planet)
        return Response(serializer.data)

    def create(self, request):
        serializer = PeopleModelSerializer(data=request.data)
        if serializer.is_valid():
            PlanetSerializer.create(serializer.validated_data)
            return Response(status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class PeopleModelViewSet(viewsets.ModelViewSet):

    serializer_class = PeopleSerializer
    queryset = People.objects.all()
    # Public
    # permission_classes

    def list(self, request):
        serializer = PeopleSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        people = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = PeopleSerializer(people)
        return Response(serializer.data)

    def create(self, request):
        serializer = PeopleModelSerializer(data=request.data)
        if serializer.is_valid():
            PeopleSerializer.create(serializer.validated_data)
            return Response(status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

