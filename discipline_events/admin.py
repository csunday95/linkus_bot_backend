from django.contrib import admin
from .models import *


@admin.register(UserDisciplineType)
class UserDisciplineTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(UserDisciplineEvent)
class UserDisciplineEventAdmin(admin.ModelAdmin):
    list_display = [
        'short_uuid',
        'discord_guild_name',
        'username_when_disciplined',
        'moderator_username',
        'discipline_type',
        'discipline_start_date_time',
        'discipline_end_date_time',
        'is_terminated',
        'is_pardoned'
    ]
    search_fields = [
        'discord_user_snowflake', 'discipline_type', 'username_when_disciplined', 'moderator_user_snowflake'
    ]
    list_filter = [
        'discipline_type',
        'is_pardoned',
        'discord_guild_name',
        'moderator_username',
        'discord_guild_snowflake',
        'moderator_user_snowflake'
    ]
    readonly_fields = [
        'discipline_type',
        'discipline_content',
        'discord_user_snowflake',
        'username_when_disciplined',
        'moderator_user_snowflake',
        'discipline_start_date_time',
        'is_terminated'
    ]

    @staticmethod
    def short_uuid(instance: UserDisciplineEvent):
        short = str(instance.id)
        short = short[:6] + '...' + short[-6:]
        return short
    short_uuid.short_description = 'UUID'
