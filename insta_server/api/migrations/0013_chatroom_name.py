# Generated by Django 4.0.4 on 2022-05-20 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_remove_chatroom_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]