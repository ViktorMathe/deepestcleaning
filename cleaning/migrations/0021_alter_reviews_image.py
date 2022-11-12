# Generated by Django 4.1.2 on 2022-11-12 13:13

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cleaning', '0020_alter_reviews_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, default=' ', max_length=255, verbose_name='image'),
        ),
    ]
