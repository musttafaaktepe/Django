# Generated by Django 4.1.4 on 2022-12-30 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='age',
        ),
    ]
