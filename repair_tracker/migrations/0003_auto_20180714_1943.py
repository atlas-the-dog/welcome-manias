# Generated by Django 2.0.7 on 2018-07-14 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair_tracker', '0002_auto_20180714_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='purchase_date',
            field=models.DateField(verbose_name='purchased date'),
        ),
    ]
