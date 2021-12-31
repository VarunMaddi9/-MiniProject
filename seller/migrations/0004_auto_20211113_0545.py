# Generated by Django 3.2.9 on 2021-11-13 05:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_auto_20211113_0521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 13, 5, 45, 43, 893439, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='seller',
            name='productimage',
            field=models.ImageField(upload_to='pics'),
        ),
    ]
