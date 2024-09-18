# Generated by Django 5.0.7 on 2024-09-01 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_service_allow_max_configurations_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='serviceconfiguration',
            options={'ordering': ['user', 'value_for_step__service', 'set_idx']},
        ),
        migrations.AlterModelOptions(
            name='serviceconfigurationstep',
            options={'ordering': ['service', 'index']},
        ),
        migrations.AddField(
            model_name='serviceconfigurationstep',
            name='query_id',
            field=models.CharField(default='slug', max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='serviceconfigurationstep',
            name='check_regex',
            field=models.CharField(blank=True, max_length=512),
        ),
    ]
