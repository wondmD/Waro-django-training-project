# Generated by Django 4.1 on 2022-12-03 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_postroom_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postroom',
            name='post_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
