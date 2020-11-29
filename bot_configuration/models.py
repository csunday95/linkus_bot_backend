from django.db import models

"""
 - moderation channel / moderation role
 - moderation channel only
 - logging channel
 - 
 - default description append format text on add/create
 - if multiple mappings for one emote are allowed
 - if multiple mappings for one role are allowed
"""

DESCRIPTION_LINE_MAX_LENGTH = 64


class BotGuildConfiguration(models.Model):
    guild_snowflake = models.BigIntegerField(
        primary_key=True,
        verbose_name='Guild Snowflake',
        help_text='The unique Guild that this configuration is for'
    )
    logging_channel_snowflake = models.BigIntegerField(
        verbose_name='Logging Channel Snowflake',
        help_text='The channel that errors and feedback messages will be logged to'
    )


class DisciplineSubConfiguration(models.Model):

    owning_configuration = models.ForeignKey(
        BotGuildConfiguration,
        on_delete=models.CASCADE,
        verbose_name='Owning Configuration',
        help_text='The configuration this sub-config belongs to'
    )
    moderation_channel_snowflake = models.BigIntegerField(
        verbose_name='Moderation Channel Snowflake',
        help_text='The snowflake of the channel for moderation commands'
    )
    moderation_role_snowflake = models.BigIntegerField(
        verbose_name='Moderation Role Snowflake',
        help_text='The role required for moderation commands to be used'
    )
    moderation_channel_only = models.BooleanField(
        default=True,
        verbose_name='Moderation Channel Only',
        help_text='If True, commands will only function in the moderation channel, regardless of user role'
    )


class ReactionSubConfiguration(models.Model):
    default_description_line = models.CharField(
        max_length=DESCRIPTION_LINE_MAX_LENGTH,
        verbose_name='Default Description Line',
        help_text='The default line that will be used with emote mappings; can include {emoji} and {role}'
    )
    allow_multiple_emotes_per_role = models.BooleanField(
        default=False,
        verbose_name='Allow Multiple Emotes Per Role',
        help_text='If True, multiple emotes can map to the same role on a reaction role embed'
    )
    allow_multiple_roles_per_emote = models.BooleanField(
        default=False,
        verbose_name='Allow Multiple Roles Per Emote',
        help_text='If True, a single emote can map to multiple roles on a reaction role embed'
    )
