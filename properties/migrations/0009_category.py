# Generated by Django 4.0.4 on 2022-05-19 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0008_alter_buyproperty_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
