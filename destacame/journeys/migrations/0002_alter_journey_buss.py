# Generated by Django 3.2.12 on 2022-03-13 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buses', '0002_rename_buss_buss2'),
        ('journeys', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='buss',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buses.buss2'),
        ),
    ]