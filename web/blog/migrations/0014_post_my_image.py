# Generated by Django 2.1.5 on 2019-01-23 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20190122_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='my_image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]