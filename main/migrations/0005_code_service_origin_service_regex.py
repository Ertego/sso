# Generated by Django 5.0.7 on 2024-08-02 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_service_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='origin',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='regex',
            field=models.BooleanField(default=False),
        ),
    ]
