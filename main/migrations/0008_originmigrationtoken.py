# Generated by Django 5.0.7 on 2024-08-04 20:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_user_codes'),
    ]

    operations = [
        migrations.CreateModel(
            name='OriginMigrationToken',
            fields=[
                ('token', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('expires', models.DateTimeField()),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.service')),
            ],
        ),
    ]
