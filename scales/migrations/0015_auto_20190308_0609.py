# Generated by Django 2.1.7 on 2019-03-08 06:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scales', '0014_auto_20190308_0335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raise',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 8, 6, 9, 28, 550128)),
        ),
    ]
