# Generated by Django 4.1.2 on 2022-11-01 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cleaning', '0005_reviews_excerpt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='author',
            new_name='name',
        ),
    ]
