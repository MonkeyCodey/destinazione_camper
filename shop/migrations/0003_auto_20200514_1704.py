# Generated by Django 3.0.6 on 2020-05-14 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200514_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='prezzo',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='altezza',
            field=models.CharField(default='', max_length=100),
        ),
    ]