from django.contrib import admin
from .models import TrackedReactionRoleEmbed, ReactionRoleEmojiMapping


@admin.register(TrackedReactionRoleEmbed)
class TrackedReactionRoleEmbedAdmin(admin.ModelAdmin):
    list_display = ['alias', 'message_snowflake', 'guild_snowflake', 'creating_member_snowflake', 'creation_time']
    search_fields = ['alias', 'guild_snowflake', 'message_snowflake', 'creating_member_snowflake', 'creation_time']
    list_filter = ['guild_snowflake', 'creating_member_snowflake']
    readonly_fields = ['creating_member_snowflake', 'creation_time']


@admin.register(ReactionRoleEmojiMapping)
class ReactionRoleEmojiMappingAdmin(admin.ModelAdmin):
    list_display = ['emoji_snowflake', 'role_snowflake', 'tracked_embed']
