from django.contrib import admin
from .models import *


@admin.register(UserDisciplineType)
class UserDisciplineTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(UserDisciplineEvent)
class UserDisciplineEventAdmin(admin.ModelAdmin):
    search_fields = ['discord_user_snowflake', 'discipline_type', 'username_when_disciplined']
    list_filter = ['discipline_type', 'is_pardoned']
