# Generated by Django 4.0.4 on 2022-05-20 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_chat_body_alter_chat_reply_to_chat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='reply_to_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='api.comment'),
        ),
    ]
