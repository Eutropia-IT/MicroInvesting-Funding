# Generated by Django 3.1.7 on 2021-04-02 20:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='investment',
            name='investmentDate',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='investment',
            name='amount',
            field=models.FloatField(default=0.0),
        ),
    ]
