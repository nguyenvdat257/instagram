# Generated by Django 4.0.4 on 2022-06-03 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_alter_commentlike_profile_alter_postlike_profile_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.comment'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='type',
            field=models.CharField(choices=[('like_comment', 'like_comment'), ('mention_comment', 'mention_comment'), ('following', 'following'), ('like_post', 'like_post'), ('comment_post', 'comment_post')], max_length=20),
        ),
    ]
