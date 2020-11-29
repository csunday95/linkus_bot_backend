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

    def update(self, instance: BotGuildConfiguration, validated_data):
        """update the given instance with the new patched data"""
        instance.logging_channel_snowflake = validated_data.get(
            'logging_channel_snowflake', instance.logging_channel_snowflake
        )
        if 'discipline_configuration' in validated_data:
            new_discipline_config = validated_data['discipline_configuration']
            current_discipline_config = instance.discipline_configuration
            current_discipline_config.moderation_channel_only = new_discipline_config.get(
                'moderation_channel_only', current_discipline_config.moderation_channel_only
            )
            current_discipline_config.moderation_role_snowflake = new_discipline_config.get(
                'moderation_role_snowflake', current_discipline_config.moderation_role_snowflake
            )
            current_discipline_config.moderation_channel_only = new_discipline_config.get(
                'moderation_channel_only', current_discipline_config.moderation_channel_only
            )
            current_discipline_config.save()
        if 'reaction_configuration' in validated_data:
            new_react_config = validated_data['reaction_configuration']
            current_react_config = instance.reaction_configuration
            current_react_config.default_description_line = new_react_config.get(
                'default_description_line', current_react_config.default_description_line
            )
            current_react_config.allow_unmapped_reactions = new_react_config.get(
                'allow_unmapped_reactions', current_react_config.allow_unmapped_reactions
            )
            current_react_config.allow_multiple_emotes_per_role = new_react_config.get(
                'allow_multiple_emotes_per_role', current_react_config.allow_multiple_emotes_per_role
            )
            current_react_config.allow_multiple_roles_per_emote = new_react_config.get(
                'allow_multiple_roles_per_emote', current_react_config.allow_multiple_roles_per_emote
            )
            current_react_config.remove_roles_on_react_remove = new_react_config.get(
                'remove_roles_on_react_remove', current_react_config.remove_roles_on_react_remove
            )
            current_react_config.save()
        instance.save()
        return instance
