# Generated by Django 4.1 on 2022-11-14 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_remove_postroom_post_pic_postroom_participants'),
    ]

    operations = [
        migrations.AddField(
            model_name='postroom',
            name='post_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
