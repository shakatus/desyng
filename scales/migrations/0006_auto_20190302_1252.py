# Generated by Django 2.1.7 on 2019-03-02 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scales', '0005_auto_20190302_0131'),
    ]

    operations = [
        migrations.AddField(
            model_name='scale',
            name='latitud',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='scale',
            name='longitud',
            field=models.CharField(default='', max_length=50),
        ),
    ]
