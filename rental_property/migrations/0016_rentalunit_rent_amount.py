# Generated by Django 4.0.2 on 2022-03-24 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental_property', '0015_alter_maintanancenotice_maintanance_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentalunit',
            name='rent_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
    ]