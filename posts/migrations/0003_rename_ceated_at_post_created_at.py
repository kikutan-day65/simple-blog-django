# Generated by Django 4.1.7 on 2023-03-03 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_rename_posts_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='ceated_at',
            new_name='created_at',
        ),
    ]