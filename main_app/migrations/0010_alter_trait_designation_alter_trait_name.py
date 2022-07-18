# Generated by Django 4.0.6 on 2022-07-18 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_sigother_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trait',
            name='designation',
            field=models.CharField(max_length=100, verbose_name='Is this trait:'),
        ),
        migrations.AlterField(
            model_name='trait',
            name='name',
            field=models.CharField(choices=[('P', 'Positive'), ('B', 'Negative'), ('N', 'Neutral')], default='P', max_length=1),
        ),
    ]