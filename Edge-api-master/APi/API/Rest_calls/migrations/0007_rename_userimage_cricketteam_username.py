# Generated by Django 4.1.5 on 2023-05-25 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Rest_calls', '0006_remove_challenges_id_challenges_challenge_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cricketteam',
            old_name='userImage',
            new_name='userName',
        ),
    ]