# Generated by Django 4.2.7 on 2023-11-18 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_photo',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
