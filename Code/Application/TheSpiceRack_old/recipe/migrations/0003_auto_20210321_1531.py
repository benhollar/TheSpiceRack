# Generated by Django 3.1.7 on 2021-03-21 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_auto_20210318_0452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='user_id',
        ),
        migrations.AddField(
            model_name='recipe',
            name='username',
            field=models.CharField(default='', max_length=200),
        ),
    ]
