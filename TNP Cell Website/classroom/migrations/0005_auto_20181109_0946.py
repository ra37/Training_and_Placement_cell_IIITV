# Generated by Django 2.1.2 on 2018-11-09 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0004_auto_20181109_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='offer',
            field=models.CharField(choices=[('Job', 'Job'), ('Internship', 'Internship'), ('Job + Internship', 'Job + Internship')], default=1, max_length=50),
        ),
        migrations.AlterField(
            model_name='job',
            name='selection_process',
            field=models.CharField(choices=[('Shortlisting from Resumes', 'Shortlisting from Resumes'), ('Written Test = Aptitude', 'Written Test - Aptitude'), ('Group Discussion', 'Group Discussion'), ('Personal Interview (Technical + HR)', 'Personal Interview (Technical + HR)'), ('Written Test - Technical', 'Written Test - Technical')], default=1, max_length=50),
        ),
    ]
