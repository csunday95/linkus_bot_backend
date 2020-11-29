from django.contrib import admin
from .models import *


@admin.register(BotGuildConfiguration)
class BotGuildConfigurationAdmin(admin.ModelAdmin):
    pass


@admin.register(DisciplineSubConfiguration)
class DisciplineSubConfigurationAdmin(admin.ModelAdmin):
    pass


@admin.register(ReactionSubConfiguration)
class ReactionSubConfigurationAdmin(admin.ModelAdmin):
    pass
