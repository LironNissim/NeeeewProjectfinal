# Generated by Django 4.0.6 on 2022-09-20 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='createdTime',
        ),
    ]