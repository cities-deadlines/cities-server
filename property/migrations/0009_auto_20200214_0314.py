# Generated by Django 3.0.3 on 2020-02-14 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20200214_0307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='name',
            field=models.CharField(default='Property 884e4cfe', max_length=20, verbose_name='Name'),
        ),
    ]