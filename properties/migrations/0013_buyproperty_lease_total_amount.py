# Generated by Django 4.0.4 on 2022-05-20 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0012_buyproperty_lease_complete_in_years'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyproperty',
            name='lease_total_amount',
            field=models.IntegerField(default=0),
        ),
    ]