# Generated by Django 4.1.4 on 2022-12-21 07:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_homework'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='date_now',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homework',
            name='is_finished',
            field=models.BooleanField(default=False),
        ),
    ]
