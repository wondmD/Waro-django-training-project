# Generated by Django 4.1 on 2022-12-05 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
