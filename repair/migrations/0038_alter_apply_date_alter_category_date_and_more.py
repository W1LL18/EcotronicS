# Generated by Django 4.1.3 on 2025-02-12 17:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0037_alter_apply_date_alter_category_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2025, 2, 12, 12, 36, 43, 858896)),
        ),
        migrations.AlterField(
            model_name='category',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2025, 2, 12, 12, 36, 43, 858896)),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2025, 2, 12, 12, 36, 43, 856901)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2025, 2, 12, 12, 36, 43, 858896)),
        ),
    ]
