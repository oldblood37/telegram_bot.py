# Generated by Django 3.2.25 on 2024-05-16 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saite', '0004_auto_20240516_2311'),
        ('telegram_auth', '0005_parsersetting'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parsersetting',
            name='group_tag',
        ),
        migrations.RemoveField(
            model_name='parsersetting',
            name='keywords',
        ),
        migrations.AddField(
            model_name='parsersetting',
            name='parser',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='parser_settings', to='saite.parser'),
            preserve_default=False,
        ),
    ]
