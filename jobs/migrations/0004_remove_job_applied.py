# Generated by Django 4.1.7 on 2023-04-05 03:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_job_applied'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='applied',
        ),
    ]
