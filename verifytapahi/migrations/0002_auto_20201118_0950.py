# Generated by Django 3.1.1 on 2020-11-18 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verifytapahi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='order_number',
            field=models.CharField(max_length=20),
        ),
    ]
