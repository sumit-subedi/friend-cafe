# Generated by Django 3.1.3 on 2020-12-19 03:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_remove_order_qty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('test_name', models.CharField(default='', max_length=200)),
                ('test_subject', models.CharField(default='', max_length=100)),
                ('test_type', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='mr', max_length=3)),
                ('name', models.CharField(default='', max_length=50)),
                ('address', models.CharField(default='', max_length=200)),
                ('city', models.CharField(default='', max_length=100)),
                ('tests', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.test')),
            ],
        ),
    ]
