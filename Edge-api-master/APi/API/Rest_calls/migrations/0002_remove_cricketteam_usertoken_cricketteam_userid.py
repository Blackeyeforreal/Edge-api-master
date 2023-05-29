# Generated by Django 4.1.5 on 2023-04-28 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Rest_calls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cricketteam',
            name='userToken',
        ),
        migrations.AddField(
            model_name='cricketteam',
            name='userId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]