# Generated by Django 4.1.5 on 2023-05-02 12:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Rest_calls', '0004_rename_userregion_cricketteam_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challenger_team_id', models.PositiveIntegerField(max_length=30)),
                ('date_and_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='challenged at')),
                ('pitch_type', models.CharField(max_length=23)),
            ],
        ),
    ]
