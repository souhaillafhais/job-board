# Generated by Django 5.0.4 on 2024-05-21 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0017_job_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='user',
            new_name='owner',
        ),
    ]