from rest_framework import viewsets
from .serializers import *
from .models import *


class BotGuildConfigurationViewSet(viewsets.ModelViewSet):
    queryset = BotGuildConfiguration.objects.all()
    serializer_class = BotGuildConfigurationSerializer


class DisciplineSubConfigurationViewSet(viewsets.ModelViewSet):
    queryset = DisciplineSubConfiguration.objects.all()
    serializer_class = DisciplineSubConfigurationSerializer


class ReactionSubConfigurationViewSet(viewsets.ModelViewSet):
    queryset = ReactionSubConfiguration.objects.all()
    serializer_class = ReactionSubConfigurationSerializer
