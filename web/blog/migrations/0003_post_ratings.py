# Generated by Django 2.1.5 on 2019-01-21 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ratings',
            field=models.IntegerField(null=True),
        ),
    ]
