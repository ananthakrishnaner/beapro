# Generated by Django 3.2.11 on 2022-02-09 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_studentprofile_about_me'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='language_spoken',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]