from django.db import models

DISCIPLINE_NAME_MAX_LENGTH = 128
USERNAME_MAX_LENGTH = 256


class UserDisciplineType(models.Model):
    """so far we have, 'muted', 'kicked', 'banned'?"""
    class Meta:
        verbose_name_plural = 'User Discipline Types'

    discipline_name = models.CharField(
        max_length=DISCIPLINE_NAME_MAX_LENGTH,
        unique=True
    )

    def __str__(self):
        return self.discipline_name

    def __repr__(self):
        return str(self)


class UserDisciplineEvent(models.Model):
    class Meta:
        verbose_name_plural = 'User Discipline Events'

    discord_user_snowflake = models.BigIntegerField(
        verbose_name='Disciplined Discord User Snowflake',
        help_text='the Discord snowflake of the user discipline by this instance'
    )
    discipline_type = models.ForeignKey(
        UserDisciplineType,
        on_delete=models.SET_NULL,
        null=True,
        help_text='the type of discipline this instance represents'
    )
    username_when_disciplined = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        verbose_name='Username When Disciplined',
        help_text='The username of the user at the time of the issuance of this discipline'
    )
    moderator_user_snowflake = models.BigIntegerField(
        verbose_name='Moderator Discord User Snowflake',
        help_text='The Discord snowflake of the moderator performing the discipline'
    )
    reason_for_discipline = models.TextField(
        verbose_name='Reason for Discipline',
        help_text='The reason for this discipline instance'
    )
    discipline_end_date_time = models.DateTimeField(
        verbose_name='Discipline End Date/Time',
        help_text='The time at which this discipline will be removed automatically; if empty, discipline is permanent',
        null=True,
        blank=True
    )
    is_pardoned = models.BooleanField(
        verbose_name='Is Pardoned',
        help_text='If checked, this user has been pardoned and this discipline is not in effect'
    )

    def __str__(self):
        s = '{} [{}] - {}'.format(
            self.username_when_disciplined,
            self.discord_user_snowflake,
            self.discipline_type.discipline_name
        )
        if self.discipline_end_date_time is not None:
            s += ' until {}'.format(self.discipline_end_date_time)
        if self.is_pardoned:
            s += ' (PARDONED)'
        return s

    def __repr__(self):
        return str(self)
