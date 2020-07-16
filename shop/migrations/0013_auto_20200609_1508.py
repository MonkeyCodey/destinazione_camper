# Generated by Django 3.0.6 on 2020-06-09 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20200609_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemimage',
            name='all_items',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Item'),
        ),
        migrations.AlterField(
            model_name='itemimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='shop/images/'),
        ),
    ]