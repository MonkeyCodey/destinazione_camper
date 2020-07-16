# Generated by Django 3.0.6 on 2020-06-11 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20200611_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameField(
            model_name='item',
            old_name='immagini',
            new_name='immagine_principale',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]