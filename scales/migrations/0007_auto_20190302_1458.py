# Generated by Django 2.1.7 on 2019-03-02 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scales', '0006_auto_20190302_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raise',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
