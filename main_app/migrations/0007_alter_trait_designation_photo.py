# Generated by Django 4.0.6 on 2022-07-18 00:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_trait_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trait',
            name='designation',
            field=models.CharField(max_length=100, verbose_name='How would you designate this trait - positive, negative, neutral, etc.?'),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('sigOther', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.sigother')),
            ],
        ),
    ]