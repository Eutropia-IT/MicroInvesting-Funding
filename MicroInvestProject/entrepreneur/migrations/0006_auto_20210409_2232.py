# Generated by Django 3.1.7 on 2021-04-09 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrepreneur', '0005_projects_proj_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='proj_Funded',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='projects',
            name='proj_details',
            field=models.TextField(),
        ),
    ]