# Generated by Django 4.1.2 on 2022-10-31 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cleaning', '0002_reviews_author_alter_reviews_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
