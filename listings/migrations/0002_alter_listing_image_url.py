# Generated by Django 4.2.7 on 2024-01-24 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image_url',
            field=models.CharField(max_length=255),
        ),
    ]
