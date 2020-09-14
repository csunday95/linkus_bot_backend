from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import *
from .models import *


class UserDisciplineTypeViewSet(viewsets.ModelViewSet):
    queryset = UserDisciplineType.objects.all()
    serializer_class = UserDisciplineTypeSerializer

    @action(detail=False)
    def get_by_name(self, request: Request):
        params = request.query_params
        name = params['name']
        try:
            disc_type = UserDisciplineType.objects.get(discipline_name=name)
        except UserDisciplineType.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(disc_type)
        return Response(serializer.data)


class UserDisciplineEventViewSet(viewsets.ModelViewSet):
    queryset = UserDisciplineEvent.objects.all()
    serializer_class = UserDisciplineEventSerializer
