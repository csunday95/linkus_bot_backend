from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *


class UserDisciplineTypeViewSet(viewsets.ModelViewSet):
    queryset = UserDisciplineType.objects.all()
    serializer_class = UserDisciplineTypeSerializer


class UserDisciplineEventViewSet(viewsets.ModelViewSet):
    queryset = UserDisciplineEvent.objects.all()
    serializer_class = UserDisciplineEventSerializer
