# Generated by Django 3.0.3 on 2020-02-08 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200208_1900'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='userId',
            new_name='id',
        ),
    ]