# Generated by Django 3.2.12 on 2022-03-13 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0001_initial'),
        ('journeys', '0002_alter_journey_buss'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='routes.route'),
        ),
    ]
