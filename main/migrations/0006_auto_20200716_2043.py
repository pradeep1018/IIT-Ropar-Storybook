# Generated by Django 3.0.6 on 2020-07-16 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_studentdetails_wallmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_format',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
