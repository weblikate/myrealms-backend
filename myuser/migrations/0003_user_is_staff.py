# Generated by Django 2.2.15 on 2020-08-23 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0002_auto_20200821_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Is Staff'),
        ),
    ]
