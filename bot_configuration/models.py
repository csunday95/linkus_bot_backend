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


class DisciplineSubConfiguration(models.Model):
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
    allow_unmapped_reactions = models.BooleanField(
        verbose_name='Allow Unmapped Reactions',
        help_text='if True, we allow unmapped emotes to remain as reactions on the reaction role embed'
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
    remove_roles_on_react_remove = models.BooleanField(
        default=False,
        verbose_name='Remove Roles on React Remove',
        help_text='If True, remove the corresponding role from all that have it if the emoji mapping is removed'
    )


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
    discipline_configuration = models.OneToOneField(
        DisciplineSubConfiguration,
        on_delete=models.CASCADE,
        verbose_name='Discipline Configuration',
        help_text='The discipline sub-configuration for this guild configuration'
    )
    reaction_configuration = models.OneToOneField(
        ReactionSubConfiguration,
        on_delete=models.CASCADE,
        verbose_name='Reaction Configuration',
        help_text='The reaction roles sub-configuration for this guild configuration'
    )
