# Generated by Django 4.0.3 on 2023-01-24 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='name',
        ),
    ]