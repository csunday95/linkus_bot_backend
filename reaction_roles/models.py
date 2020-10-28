from django.db import models


# Create your models here.
class TrackedReactionRoleEmbed(models.Model):
    message_snowflake = models.BigIntegerField(
        primary_key=True,
        verbose_name='Message Snowflake',
        help_text='The discord snowflake for the tracked reaction roles embed'
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


class ReactionRoleEmojiMapping(models.Model):
    tracked_embed = models.ForeignKey(
        TrackedReactionRoleEmbed,
        on_delete=models.CASCADE,
        verbose_name='Tracked Embed',
        help_text='The reaction role embed this mapping is relevant for',
        related_name='role_emoji_mappings'
    )
    role_snowflake = models.BigIntegerField(
        verbose_name='Role Snowflake',
        help_text='The snowflake of the role for this mapping entry'
    )
    emoji_snowflake = models.BigIntegerField(
        verbose_name='Emoji Snowflake',
        help_text='The snowflake of the emoji for this mapping entry'
    )
