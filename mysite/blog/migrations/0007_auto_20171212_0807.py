# Generated by Django 2.0 on 2017-12-12 13:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20171211_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 12, 13, 7, 46, 124952, tzinfo=utc)),
        ),
    ]
