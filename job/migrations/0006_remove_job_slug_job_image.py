# Generated by Django 5.1 on 2024-09-14 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_job_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='slug',
        ),
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(default='', height_field=82, upload_to='jobs/', width_field=82),
            preserve_default=False,
        ),
    ]
