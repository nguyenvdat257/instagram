# Generated by Django 4.0.4 on 2022-06-13 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0037_profile_last_activity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='last_activity',
            new_name='last_active',
        ),
    ]
