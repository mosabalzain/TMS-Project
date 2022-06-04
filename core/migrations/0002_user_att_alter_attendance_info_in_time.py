# Generated by Django 4.0.4 on 2022-06-01 10:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='att',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.attendance_info'),
        ),
        migrations.AlterField(
            model_name='attendance_info',
            name='in_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 1, 12, 7, 53, 374366)),
        ),
    ]