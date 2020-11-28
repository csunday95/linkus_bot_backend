
from rest_framework import serializers
from .models import TrackedReactionRoleEmbed, ReactionRoleEmojiMapping


class TrackedReactionRoleEmbedSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackedReactionRoleEmbed
        fields = '__all__'
        read_only_fields = ['creation_time']

    def to_representation(self, instance: TrackedReactionRoleEmbed):
        data = super().to_representation(instance)
        mapping_serializer = ReactionRoleEmojiMappingSerializer(instance=instance.role_emoji_mappings.all(), many=True)
        data['mappings'] = mapping_serializer.data
        return data

    def to_internal_value(self, data):
        mappings_list = data.get('mappings')
        if mappings_list is None:
            raise serializers.ValidationError('"mappings" field is required')
        mapping_serializer = ReactionRoleEmojiMappingSerializer(data=mappings_list, many=True)
        if not mapping_serializer.is_valid():
            fmt = 'encountered an error deserializing mappings list: {}'
            raise serializers.ValidationError(fmt.format(mapping_serializer.errors))
        try:
            return {
                'message_snowflake': data['message_snowflake'],
                'guild_snowflake': data['guild_snowflake'],
                'alias': data['alias'],
                'creating_member_snowflake': data['creating_member_snowflake'],
                'mappings': mapping_serializer.validated_data
            }
        except KeyError as e:
            raise serializers.ValidationError(f'Missing a required field: {e}')

    def create(self, validated_data):
        mapping_list = validated_data.pop('mappings')
        created_tracked_embed = super().create(validated_data)
        for mapping in mapping_list:  # type: dict
            mapping['tracked_embed'] = created_tracked_embed
            ReactionRoleEmojiMapping.objects.create(**mapping)
        return created_tracked_embed


class ReactionRoleEmojiMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReactionRoleEmojiMapping
        fields = ['role_snowflake', 'emoji_snowflake']
