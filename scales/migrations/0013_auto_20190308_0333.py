# Generated by Django 2.1.7 on 2019-03-08 03:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scales', '0012_remove_raise_codigo'),
    ]

    operations = [
        migrations.AddField(
            model_name='raise',
            name='codigo',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='scale',
            name='point',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scales.Point'),
        ),
    ]
