# Generated by Django 3.0.6 on 2020-06-02 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20200602_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='titolo',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
