# Generated by Django 3.1.1 on 2020-09-12 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDisciplineType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discipline_name', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserDisciplineEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discord_user_snowflake', models.CharField(help_text='the Discord snowflake of the user discipline by this instance', max_length=128, verbose_name='Discord User Snowflake')),
                ('username_when_disciplined', models.CharField(help_text='The username of the user at the time of the issuance of this discipline', max_length=256, verbose_name='Username When Disciplined')),
                ('reason_for_discipline', models.TextField(help_text='The reason for this discipline instance', verbose_name='Reason for Disciplined')),
                ('discipline_end_date_time', models.DateTimeField(help_text='The time at which this discipline will be removed automatically', verbose_name='Discipline End Date/Time')),
                ('is_pardoned', models.BooleanField(help_text='If checked, this user has been pardoned and this discipline is not in effect', verbose_name='Is Pardoned')),
                ('discipline_type', models.ForeignKey(help_text='the type of discipline this instance represents', null=True, on_delete=django.db.models.deletion.SET_NULL, to='linkus_bot.userdisciplinetype')),
            ],
        ),
    ]
