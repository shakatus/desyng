# Generated by Django 2.1.7 on 2019-03-09 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scales', '0019_auto_20190309_0648'),
    ]

    operations = [
        migrations.RenameField(
            model_name='raise',
            old_name='scale_id',
            new_name='scale',
        ),
    ]