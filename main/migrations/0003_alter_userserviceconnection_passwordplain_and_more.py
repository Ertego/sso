# Generated by Django 4.0 on 2021-12-26 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_service_userserviceconnection_user_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userserviceconnection',
            name='passwordPlain',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='userserviceconnection',
            name='username',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
