# Generated by Django 4.0.4 on 2022-05-20 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_chatroom_updated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postseen',
            old_name='chat',
            new_name='post',
        ),
    ]
