# Generated by Django 4.1.5 on 2023-01-22 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='income',
            name='name',
        ),
    ]
