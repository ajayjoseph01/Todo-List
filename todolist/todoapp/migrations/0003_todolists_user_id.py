# Generated by Django 3.2.8 on 2022-05-28 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_todolists_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolists',
            name='user_id',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]
