# Generated by Django 4.1.7 on 2023-03-12 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dream',
            fields=[
                ('id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=15)),
                ('quote', models.TextField()),
            ],
        ),
    ]