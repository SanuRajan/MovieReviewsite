# Generated by Django 2.1.5 on 2019-01-22 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190122_0643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='my_genre_field',
            field=models.IntegerField(choices=[(1, 'Horror'), (2, 'Sci-fiction'), (3, 'Thriller'), (4, 'Action')], max_length=100, null=True),
        ),
    ]