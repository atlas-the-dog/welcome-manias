# Generated by Django 2.0.7 on 2018-07-14 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair_tracker', '0003_auto_20180714_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='repair_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='repaired date'),
        ),
    ]