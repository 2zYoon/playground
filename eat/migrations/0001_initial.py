# Generated by Django 3.2.9 on 2021-12-10 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=64)),
                ('restaurant', models.CharField(max_length=64)),
                ('food', models.CharField(max_length=128)),
                ('date', models.IntegerField()),
                ('score', models.DateTimeField(auto_now=True)),
                ('review', models.TextField()),
            ],
        ),
    ]
