# Generated by Django 4.0.4 on 2022-05-27 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_rename_video_image_post_video_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comments_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='likes_count',
            field=models.IntegerField(default=0),
        ),
    ]
