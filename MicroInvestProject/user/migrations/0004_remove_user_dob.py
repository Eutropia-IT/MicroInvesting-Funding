# Generated by Django 3.1.7 on 2021-03-25 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210326_0201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='dob',
        ),
    ]