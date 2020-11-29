from rest_framework import serializers
from .models import DisciplineSubConfiguration, BotGuildConfiguration, ReactionSubConfiguration


class BotGuildConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotGuildConfiguration
        field = '__all__'
        depth = 1


class DisciplineSubConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisciplineSubConfiguration
        field = '__all__'


class ReactionSubConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReactionSubConfiguration
        field = '__all__'
