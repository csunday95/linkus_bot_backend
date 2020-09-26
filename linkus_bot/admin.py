from django.contrib import admin
from .models import *


@admin.register(UserDisciplineType)
class UserDisciplineTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(UserDisciplineEvent)
class UserDisciplineEventAdmin(admin.ModelAdmin):
    list_display = [
        'username_when_disciplined',
        'discipline_type',
        'discipline_start_date_time',
        'discipline_end_date_time',
        'is_terminated',
        'is_pardoned'
    ]
    search_fields = ['discord_user_snowflake', 'discipline_type', 'username_when_disciplined']
    list_filter = ['discipline_type', 'is_pardoned']
    readonly_fields = [
        'discipline_type',
        'discipline_content',
        'discord_user_snowflake',
        'username_when_disciplined',
        'moderator_user_snowflake',
        'discipline_start_date_time',
        'is_terminated'
    ]
