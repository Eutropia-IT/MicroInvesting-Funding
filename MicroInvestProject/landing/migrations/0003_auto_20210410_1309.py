# Generated by Django 3.1.7 on 2021-04-10 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_resetpssdb_secritkey'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resetpssdb',
            old_name='joiningDate',
            new_name='date',
        ),
    ]
