# Generated by Django 4.1.7 on 2023-02-25 21:55

from django.db import migrations, models
import web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_delete_firmware'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='displayOrder',
            field=models.IntegerField(default=web.models.Room.number),
        ),
    ]
