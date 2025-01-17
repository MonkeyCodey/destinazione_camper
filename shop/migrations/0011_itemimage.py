# Generated by Django 3.0.6 on 2020-06-08 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_item_titolo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('camper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shop.Item')),
            ],
        ),
    ]
