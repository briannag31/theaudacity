# Generated by Django 4.0.6 on 2022-07-14 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meetings',
            old_name='sig_other',
            new_name='relationship',
        ),
    ]
