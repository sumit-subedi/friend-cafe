# Generated by Django 3.1.3 on 2020-12-24 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_auto_20201224_0403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordereditem',
            name='item',
        ),
        migrations.AddField(
            model_name='ordereditem',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.menu'),
        ),
    ]
