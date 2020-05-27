import json

from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import People, Planet
from .serializers import PeopleSerializer, PlanetSerializer


class PlanetModelViewSet(viewsets.ModelViewSet):

    serializer_class = PlanetSerializer
    queryset = Planet.objects.all()


class PeopleModelViewSet(viewsets.ModelViewSet):

    serializer_class = PeopleSerializer
    queryset = People.objects.all()
