# Generated by Django 4.1.5 on 2023-04-28 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Rest_calls', '0002_remove_cricketteam_usertoken_cricketteam_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cricketteam',
            name='userId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
