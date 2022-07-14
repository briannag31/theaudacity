# Generated by Django 4.0.6 on 2022-07-14 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_rename_sig_other_meetings_relationship'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trait',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='meetings',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='sigother',
            name='traits',
            field=models.ManyToManyField(to='main_app.trait'),
        ),
    ]