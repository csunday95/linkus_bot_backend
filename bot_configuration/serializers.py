from rest_framework import serializers
from .models import DisciplineSubConfiguration, BotGuildConfiguration, ReactionSubConfiguration
from django.db import transaction


class DisciplineSubConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisciplineSubConfiguration
        fields = '__all__'


class ReactionSubConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReactionSubConfiguration
        fields = '__all__'


class BotGuildConfigurationSerializer(serializers.ModelSerializer):
    discipline_configuration = DisciplineSubConfigurationSerializer()
    reaction_configuration = ReactionSubConfigurationSerializer()

    class Meta:
        model = BotGuildConfiguration
        fields = '__all__'
        read_only_fields = ['discipline_configuration', 'reaction_configuration']

    def create(self, validated_data):
        """Creates the configuration instances from provided data"""
        discipline_data = validated_data.pop('discipline_configuration')
        reaction_data = validated_data.pop('reaction_configuration')
        with transaction.atomic():
            validated_data['discipline_configuration'] = \
                DisciplineSubConfiguration.objects.create(**discipline_data)
            validated_data['reaction_configuration'] = \
                ReactionSubConfiguration.objects.create(**reaction_data)
            created_guild_config = BotGuildConfiguration.objects.create(**validated_data)
        return created_guild_config
