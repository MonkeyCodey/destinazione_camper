# Generated by Django 3.0.6 on 2020-05-17 15:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20200517_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='data_inserzione',
            field=models.DateField(default=datetime.date.today),
        ),
    ]