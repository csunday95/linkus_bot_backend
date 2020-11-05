from django.db import models


class BotGuildConfiguration(models.Model):
    guild_snowflake = models.BigIntegerField(
        primary_key=True,
        verbose_name='Guild Snowflake',
        help_text='The unique Guild that this configuration is for'
    )
