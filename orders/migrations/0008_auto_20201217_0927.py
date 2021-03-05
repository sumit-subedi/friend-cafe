# Generated by Django 3.1.3 on 2020-12-17 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20201217_0852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='table_no',
        ),
        migrations.AddField(
            model_name='order',
            name='table',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.table'),
        ),
    ]
