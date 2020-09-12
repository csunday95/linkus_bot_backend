from django.db import models

DISCIPLINE_NAME_MAX_LENGTH = 128
SNOWFLAKE_MAX_LENGTH = 128
USERNAME_MAX_LENGTH = 256


class UserDisciplineType(models.Model):
    discipline_name = models.CharField(
        max_length=DISCIPLINE_NAME_MAX_LENGTH,
        unique=True
    )


class UserDisciplineEvent(models.Model):
    discord_user_snowflake = models.CharField(
        max_length=SNOWFLAKE_MAX_LENGTH,
        verbose_name='Discord User Snowflake',
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
    reason_for_discipline = models.TextField(
        verbose_name='Reason for Disciplined',
        help_text='The reason for this discipline instance'
    )
    discipline_end_date_time = models.DateTimeField(
        verbose_name='Discipline End Date/Time',
        help_text='The time at which this discipline will be removed automatically'
    )
    is_pardoned = models.BooleanField(
        verbose_name='Is Pardoned',
        help_text='If checked, this user has been pardoned and this discipline is not in effect'
    )
