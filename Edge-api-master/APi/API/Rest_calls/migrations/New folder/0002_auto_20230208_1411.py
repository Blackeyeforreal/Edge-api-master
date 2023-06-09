# Generated by Django 3.2.3 on 2023-02-08 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Rest_calls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CricketPlayer',
            fields=[
                ('Name', models.CharField(max_length=34)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('age', models.PositiveIntegerField(max_length=90)),
                ('handed', models.CharField(max_length=8)),
                ('bowlingtype', models.CharField(max_length=10)),
                ('battingVspin', models.PositiveIntegerField(max_length=30)),
                ('battingVpace', models.PositiveIntegerField(max_length=30)),
                ('bowling', models.PositiveIntegerField(max_length=30)),
                ('experience', models.PositiveIntegerField(max_length=30)),
                ('fielding', models.PositiveIntegerField(max_length=30)),
                ('region', models.CharField(max_length=34)),
            ],
        ),
        migrations.CreateModel(
            name='CricketTeam',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('teamName', models.CharField(max_length=23)),
                ('teamIamge', models.ImageField(upload_to='')),
                ('userImage', models.CharField(max_length=23)),
                ('userToken', models.UUIDField()),
            ],
        ),
        migrations.DeleteModel(
            name='CriketPlayer',
        ),
        migrations.AddField(
            model_name='cricketplayer',
            name='TeamId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Rest_calls.cricketteam'),
        ),
    ]
