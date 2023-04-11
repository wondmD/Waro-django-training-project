# Generated by Django 4.1 on 2022-11-28 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_postroom_level'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.RemoveField(
            model_name='postroom',
            name='level',
        ),
        migrations.AlterField(
            model_name='postroom',
            name='post_image',
            field=models.ImageField(null=True, upload_to='static/base/images'),
        ),
    ]
