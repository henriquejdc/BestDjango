# Generated by Django 4.1.1 on 2022-09-19 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='active_language',
            field=models.CharField(choices=[('en-US', 'US English'), ('pt-BR', 'Português BR')], default='en-us', max_length=10, verbose_name='Active Language'),
        ),
    ]
