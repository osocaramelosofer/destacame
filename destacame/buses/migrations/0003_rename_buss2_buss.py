# Generated by Django 3.2.12 on 2022-03-13 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journeys', '0002_alter_journey_buss'),
        ('buses', '0002_rename_buss_buss2'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Buss2',
            new_name='Buss',
        ),
    ]
