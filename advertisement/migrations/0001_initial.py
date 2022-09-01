# Generated by Django 4.0.4 on 2022-06-14 08:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('properties', '0018_rename_instalment_buyproperty_monthly_instalment'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdsProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=160)),
                ('content', models.TextField()),
                ('slug', models.CharField(max_length=70, unique=True)),
                ('property_img1', models.ImageField(blank=True, null=True, upload_to='static/images/property')),
                ('property_img2', models.ImageField(blank=True, null=True, upload_to='static/images/property')),
                ('property_img3', models.ImageField(blank=True, null=True, upload_to='static/images/property')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='static/images/property')),
                ('property_price', models.IntegerField(default=0)),
                ('monthly_instalment', models.IntegerField(default=0)),
                ('advance', models.IntegerField(default=0)),
                ('lease_complete_in_years', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=240)),
                ('city', models.CharField(default='', max_length=240)),
                ('room', models.IntegerField(default=0)),
                ('bathroom', models.IntegerField(default=0)),
                ('kitchen', models.IntegerField(default=0)),
                ('floor', models.IntegerField(default=0)),
                ('marla', models.FloatField(default=0.0, max_length=4)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='properties.category')),
            ],
        ),
    ]