# Generated by Django 3.2.20 on 2023-08-03 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_task_daily'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='daily',
        ),
        migrations.AddField(
            model_name='task',
            name='activity',
            field=models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly')], default='daily', max_length=20),
        ),
    ]
