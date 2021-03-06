# Generated by Django 2.1.2 on 2018-11-08 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0003_organizationaldetails_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='offer',
            field=models.IntegerField(choices=[('Job', 'Job'), ('Internship', 'Internship'), ('Job + Internship', 'Job + Internship')], default=1),
        ),
        migrations.AlterField(
            model_name='job',
            name='selection_process',
            field=models.IntegerField(choices=[('Shortlisting from Resumes', 'Shortlisting from Resumes'), ('Written Test = Aptitude', 'Written Test - Aptitude'), ('Group Discussion', 'Group Discussion'), ('Personal Interview (Technical + HR)', 'Personal Interview (Technical + HR)'), ('Written Test - Technical', 'Written Test - Technical')], default=1),
        ),
    ]
