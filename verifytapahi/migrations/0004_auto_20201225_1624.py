# Generated by Django 3.1.1 on 2020-12-25 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verifytapahi', '0003_auto_20201224_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordercodenumber',
            name='order_number',
            field=models.IntegerField(unique=True),
        ),
    ]
