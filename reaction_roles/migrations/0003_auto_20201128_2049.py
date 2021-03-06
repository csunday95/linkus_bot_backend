# Generated by Django 3.1.3 on 2020-11-28 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reaction_roles', '0002_trackedreactionroleembed_guild_snowflake'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reactionroleemojimapping',
            options={'verbose_name_plural': 'Reaction Role Emoji Mappings'},
        ),
        migrations.AlterModelOptions(
            name='trackedreactionroleembed',
            options={'verbose_name_plural': 'Tracked Reaction Role Embeds'},
        ),
        migrations.AddField(
            model_name='trackedreactionroleembed',
            name='alias',
            field=models.CharField(default='alias', help_text='A human readable alias for this reaction role embed', max_length=64, verbose_name='Alias'),
            preserve_default=False,
        ),
        migrations.AddConstraint(
            model_name='trackedreactionroleembed',
            constraint=models.UniqueConstraint(fields=('message_snowflake', 'alias'), name='unique_alias'),
        ),
    ]
