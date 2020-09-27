from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import *
from .models import *


class UserDisciplineTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserDisciplineType.objects.all()
    serializer_class = UserDisciplineTypeSerializer

    @action(detail=False)
    def get_by_name(self, request: Request):
        params = request.query_params
        try:
            name = params['name']
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            disc_type = UserDisciplineType.objects.get(discipline_name__iexact=name)
        except UserDisciplineType.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(disc_type)
        return Response(serializer.data)


class UserDisciplineEventViewSet(viewsets.ModelViewSet):
    queryset = UserDisciplineEvent.objects.all()
    serializer_class = UserDisciplineEventSerializer

    def create(self, request, *args, **kwargs):
        serializer = CreateUserDisciplineEventSerializer(data=request.data)
        if serializer.is_valid():
            save_result = serializer.save()
            output_serializer = UserDisciplineEventSerializer(save_result)
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False)
    def get_discipline_events_for(self, request: Request):
        params = request.query_params
        try:
            user_snowflake = int(params['user_snowflake'])
        except (ValueError, TypeError, KeyError):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        events = UserDisciplineEvent.objects\
            .filter(discord_user_snowflake=user_snowflake)\
            .order_by('-discipline_start_date_time')
        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def get_latest_discipline(self, request: Request):
        params = request.query_params
        try:
            user_snowflake = int(params['user_snowflake'])
            discipline_name = params['discipline_name']
        except (ValueError, TypeError, KeyError):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            latest_discipline = UserDisciplineEvent.objects\
                .filter(discord_user_snowflake=user_snowflake,
                        discipline_type__discipline_name__iexact=discipline_name)\
                .latest('discipline_start_date_time')
        except UserDisciplineEvent.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(self.get_serializer(latest_discipline).data)

    @action(detail=False)
    def get_latest_discipline_by_username(self, request: Request):
        params = request.query_params
        try:
            username = params['username']
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            latest_relevant_event = UserDisciplineEvent.objects.filter(
                username_when_disciplined__iexact=username
            ).latest('discipline_start_date_time')
        except UserDisciplineEvent.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(self.get_serializer(latest_relevant_event).data)
