# Generated by Django 4.0.4 on 2022-06-21 04:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0044_alter_profile_last_view_page_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='last_view_page_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
