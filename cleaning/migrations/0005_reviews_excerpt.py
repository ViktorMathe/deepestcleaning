# Generated by Django 4.1.2 on 2022-11-01 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cleaning', '0004_remove_reviews_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='excerpt',
            field=models.TextField(blank=True),
        ),
    ]