# Generated by Django 2.1.5 on 2019-01-21 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190121_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='ratings',
            field=models.IntegerField(null=True),
        ),
    ]
