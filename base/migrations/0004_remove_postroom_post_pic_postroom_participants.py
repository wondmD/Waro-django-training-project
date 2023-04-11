# Generated by Django 4.1 on 2022-11-02 16:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0003_alter_postroom_options_postroom_post_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postroom',
            name='post_pic',
        ),
        migrations.AddField(
            model_name='postroom',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='participants', to=settings.AUTH_USER_MODEL),
        ),
    ]
