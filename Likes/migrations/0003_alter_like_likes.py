# Generated by Django 4.1.7 on 2023-02-26 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Likes', '0002_alter_like_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='likes',
            field=models.BooleanField(default=False),
        ),
    ]