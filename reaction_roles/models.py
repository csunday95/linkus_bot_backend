from django.db import models


class TrackedReactionRoleEmbed(models.Model):
    class Meta:
        verbose_name_plural = 'Tracked Reaction Role Embeds'

    message_snowflake = models.BigIntegerField(
        primary_key=True,
        verbose_name='Message Snowflake',
        help_text='The discord snowflake for the tracked reaction roles embed'
    )
    guild_snowflake = models.BigIntegerField(
        verbose_name='Guild Snowflake',
        help_text='The guild within which this reaction role embed exists'
    )
    creating_member_snowflake = models.BigIntegerField(
        verbose_name='Creating Member Snowflake',
        help_text='The discord snowflake of the user that created this instance'
    )
    creation_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Creation Time',
        help_text='The date/time this entry was created'
    )

    def __str__(self):
        return f'Reaction Role Embed M{self.message_snowflake} [G{self.guild_snowflake}]'


class ReactionRoleEmojiMapping(models.Model):
    class Meta:
        verbose_name_plural = 'Reaction Role Emoji Mappings'

    tracked_embed = models.ForeignKey(
        TrackedReactionRoleEmbed,
        on_delete=models.CASCADE,
        verbose_name='Tracked Embed',
        help_text='The reaction role embed this mapping is relevant for',
        related_name='role_emoji_mappings'
    )
    emoji_snowflake = models.BigIntegerField(
        verbose_name='Emoji Snowflake',
        help_text='The snowflake of the emoji for this mapping entry'
    )
    role_snowflake = models.BigIntegerField(
        verbose_name='Role Snowflake',
        help_text='The snowflake of the role for this mapping entry'
    )

    def __str__(self):
        return f'Emoji Mapping [{self.emoji_snowflake}] -> [{self.role_snowflake}]'
