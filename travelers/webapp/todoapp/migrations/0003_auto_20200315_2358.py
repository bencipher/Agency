# Generated by Django 3.0.3 on 2020-03-15 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_auto_20200315_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoapp',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
