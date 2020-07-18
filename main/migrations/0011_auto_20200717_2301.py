# Generated by Django 3.0.6 on 2020-07-17 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0010_auto_20200717_2150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post_info',
        ),
        migrations.RemoveField(
            model_name='post',
            name='share_num',
        ),
        migrations.AddField(
            model_name='comment',
            name='User',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cmntusr', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cmntpost', to='main.Post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True, null=True)),
                ('User', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='likeusr', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='likedpost', to='main.Post')),
            ],
        ),
    ]
