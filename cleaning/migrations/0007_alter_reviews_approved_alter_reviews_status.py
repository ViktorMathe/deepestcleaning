# Generated by Django 4.1.2 on 2022-11-02 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cleaning', '0006_rename_author_reviews_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='approved',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=1),
        ),
    ]