# Generated by Django 3.2.9 on 2021-12-10 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eat', '0004_alter_eat_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eat',
            name='region',
            field=models.CharField(max_length=64),
        ),
    ]