# Generated by Django 5.0.1 on 2024-01-18 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_remove_uploadimage_caption_uploadimage_uploaded_at'),
    ]

    operations = [
        migrations.DeleteModel(
            name='uploadimage',
        ),
    ]
