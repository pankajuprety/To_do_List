# Generated by Django 4.2 on 2023-06-14 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='daily',
            field=models.BooleanField(default=True),
        ),
    ]
