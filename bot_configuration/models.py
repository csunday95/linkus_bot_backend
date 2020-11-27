from django.db import models

"""
 - moderation channel / moderation role
 - logging channel
 - 
 - default description append format text on add/create
 - if multiple mappings for one emote are allowed
 - if multiple mappings for one role are allowed
"""


class BotGuildConfiguration(models.Model):
    guild_snowflake = models.BigIntegerField(
        primary_key=True,
        verbose_name='Guild Snowflake',
        help_text='The unique Guild that this configuration is for'
    )
