# Generated by Django 3.1.3 on 2020-12-19 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20201219_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='table',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.table'),
        ),
    ]