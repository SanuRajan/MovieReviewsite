# Generated by Django 2.1.5 on 2019-01-21 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='ratings',
            field=models.IntegerField(max_length=10, null=True),
        ),
    ]
