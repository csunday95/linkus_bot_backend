# Generated by Django 3.1.1 on 2020-10-04 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkus_bot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdisciplineevent',
            name='discord_guild_name',
            field=models.CharField(default='guild', help_text='The name of the discord guild at the time of event creation', max_length=128, verbose_name='Discord Guild Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdisciplineevent',
            name='moderator_username',
            field=models.CharField(default='username', help_text="The moderator's username at the time this event was created", max_length=256, verbose_name='Moderator Username'),
            preserve_default=False,
        ),
    ]