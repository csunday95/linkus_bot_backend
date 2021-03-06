
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
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
    pagination_class = PageNumberPagination

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
            guild_snowflake = int(params['guild_snowflake'])
            user_snowflake = int(params['user_snowflake'])
        except (ValueError, TypeError, KeyError):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        events = UserDisciplineEvent.objects\
            .filter(discord_user_snowflake=user_snowflake, discord_guild_snowflake=guild_snowflake)\
            .order_by('-discipline_start_date_time')
        page = self.paginate_queryset(events)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def get_latest_discipline(self, request: Request):
        params = request.query_params
        try:
            guild_snowflake = int(params['guild_snowflake'])
            user_snowflake = int(params['user_snowflake'])
            discipline_name = params['discipline_name']
        except (ValueError, TypeError, KeyError):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            latest_discipline = UserDisciplineEvent.objects\
                .filter(discord_guild_snowflake=guild_snowflake,
                        discord_user_snowflake=user_snowflake,
                        discipline_type__discipline_name__iexact=discipline_name)\
                .latest('discipline_start_date_time')
        except UserDisciplineEvent.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(self.get_serializer(latest_discipline).data)

    @action(detail=False)
    def get_latest_discipline_by_username(self, request: Request):
        params = request.query_params
        try:
            guild_snowflake = int(params['guild_snowflake'])
            username = params['username']
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            latest_relevant_event = UserDisciplineEvent.objects.filter(
                discord_guild_snowflake=guild_snowflake,
                username_when_disciplined__iexact=username
            ).latest('discipline_start_date_time')
        except UserDisciplineEvent.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(self.get_serializer(latest_relevant_event).data)
