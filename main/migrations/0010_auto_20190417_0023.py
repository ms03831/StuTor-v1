# Generated by Django 2.1.7 on 2019-04-16 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20190416_2056'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='Pic',
            new_name='Photograph',
        ),
        migrations.RenameField(
            model_name='tutor',
            old_name='DegreeImage',
            new_name='Degree_Image',
        ),
        migrations.RenameField(
            model_name='tutor',
            old_name='Degree',
            new_name='Degree_Name',
        ),
        migrations.RenameField(
            model_name='tutor',
            old_name='Qualification',
            new_name='Highest_Qualification',
        ),
    ]
