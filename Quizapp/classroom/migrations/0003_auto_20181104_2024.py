# Generated by Django 2.1.2 on 2018-11-04 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0002_auto_20181104_2024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='orgJob',
            new_name='organization',
        ),
        migrations.RenameField(
            model_name='personaldetails',
            old_name='orgPersonal',
            new_name='organization',
        ),
    ]
