# Generated by Django 4.1.2 on 2022-11-07 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cleaning', '0009_bookingsystem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookingsystem',
            old_name='clening_type',
            new_name='cleaning_type',
        ),
    ]
