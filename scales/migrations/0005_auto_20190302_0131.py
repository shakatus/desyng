# Generated by Django 2.1.7 on 2019-03-02 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scales', '0004_auto_20190301_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='codigo',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]