# Generated by Django 2.0.6 on 2018-10-09 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('date_App', '0002_auto_20181009_1959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timesheet',
            name='pub_date',
        ),
    ]