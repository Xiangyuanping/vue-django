# Generated by Django 2.2.5 on 2022-05-19 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_gp_list'),
    ]

    operations = [
        migrations.DeleteModel(
            name='gp_list',
        ),
        migrations.DeleteModel(
            name='Gpxx',
        ),
    ]
