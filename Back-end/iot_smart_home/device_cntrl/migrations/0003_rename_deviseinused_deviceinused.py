# Generated by Django 3.2.7 on 2021-12-23 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_cntrl', '0003_remove_house_devices'),
        ('device_cntrl', '0002_deviseinused'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DeviseInUsed',
            new_name='DeviceInUsed',
        ),
    ]
