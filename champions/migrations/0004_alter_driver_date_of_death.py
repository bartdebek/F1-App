# Generated by Django 4.0.7 on 2022-08-14 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('champions', '0003_alter_driver_date_of_death'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='date_of_death',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]