# Generated by Django 4.1 on 2022-12-05 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_postroom_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gallery_image', models.ImageField(blank=True, null=True, upload_to='gallery_image/')),
                ('caption', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
