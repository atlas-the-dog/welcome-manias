# Generated by Django 2.0.7 on 2018-07-14 20:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repair_tracker', '0006_auto_20180714_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='Βλάβη',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('μαρκα', models.CharField(max_length=200)),
                ('μοντέλο', models.CharField(max_length=200)),
                ('προϊόν', models.CharField(max_length=200)),
                ('βλαβη', models.TextField()),
                ('σημειωσεις', models.TextField(blank=True)),
                ('ημερομηνία_αγοράς', models.DateField(verbose_name='ημερομηνία αγοράς')),
                ('ημερομηνία_αναφοράς', models.DateTimeField(verbose_name='ημερομηνία αναφοράς')),
                ('ημερομηνία_επισκευής', models.DateTimeField(blank=True, null=True, verbose_name='ημερομηνία επισκευής')),
            ],
        ),
        migrations.CreateModel(
            name='Πελατης',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ονομα', models.CharField(max_length=200)),
                ('επιθετο', models.CharField(max_length=200)),
                ('σταθερο', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Ο αριθμός τηλεφώνου πρέπει να είναι της μορφής: '+999999999'. Επιτρέπονται μέχρι 15 ψηφία.", regex='^\\+?1?\\d{9,15}$')])),
                ('κινητο', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Ο αριθμός τηλεφώνου πρέπει να είναι της μορφής: '+999999999'. Επιτρέπονται μέχρι 15 ψηφία.", regex='^\\+?1?\\d{9,15}$')])),
                ('αλλο', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Ο αριθμός τηλεφώνου πρέπει να είναι της μορφής: '+999999999'. Επιτρέπονται μέχρι 15 ψηφία.", regex='^\\+?1?\\d{9,15}$')])),
                ('διευθυνση', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Τεχνικος',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ονομα', models.CharField(max_length=200)),
                ('επιθετο', models.CharField(max_length=200)),
                ('σταθερό', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Ο αριθμός τηλεφώνου πρέπει να είναι της μορφής: '+999999999'. Επιτρέπονται μέχρι 15 ψηφία.", regex='^\\+?1?\\d{9,15}$')])),
                ('αλλο', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Ο αριθμός τηλεφώνου πρέπει να είναι της μορφής: '+999999999'. Επιτρέπονται μέχρι 15 ψηφία.", regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.CharField(max_length=200, validators=[django.core.validators.EmailValidator()])),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='product',
            name='repairer',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Technician',
        ),
        migrations.AddField(
            model_name='βλάβη',
            name='πελάτης',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repair_tracker.Πελατης'),
        ),
        migrations.AddField(
            model_name='βλάβη',
            name='τεχνικός',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='repair_tracker.Τεχνικος'),
        ),
    ]
