# Generated by Django 4.1.5 on 2023-05-26 08:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Rest_calls', '0007_rename_userimage_cricketteam_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenges',
            name='date_and_time',
            field=models.DateTimeField(verbose_name='challenged at'),
        ),
        migrations.CreateModel(
            name='PlayerEleven',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('player_id', models.PositiveSmallIntegerField(max_length=24)),
                ('challenge_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Rest_calls.challenges')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BowlingLineUp',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('player_id', models.PositiveSmallIntegerField(max_length=24)),
                ('challenge_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Rest_calls.challenges')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
