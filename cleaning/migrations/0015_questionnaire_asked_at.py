# Generated by Django 4.1.2 on 2022-11-08 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cleaning', '0014_alter_bookingsystem_cleaning_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='asked_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
