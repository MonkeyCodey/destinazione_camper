# Generated by Django 3.0.6 on 2020-05-17 14:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20200517_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='data_inserzione',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
