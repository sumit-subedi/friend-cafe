# Generated by Django 3.1.3 on 2020-12-17 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemId', models.IntegerField()),
                ('item', models.CharField(max_length=100)),
                ('qty', models.CharField(max_length=2)),
                ('table_no', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tableName', models.CharField(max_length=100)),
                ('occupied', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Orders',
        ),
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
