# Generated by Django 4.0.1 on 2022-06-15 12:16

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description',
            field=tinymce.models.HTMLField(default=''),
            preserve_default=False,
        ),
    ]
