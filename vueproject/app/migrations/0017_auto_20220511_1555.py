# Generated by Django 2.2.5 on 2022-05-11 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_merge_20220511_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gpxx',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
