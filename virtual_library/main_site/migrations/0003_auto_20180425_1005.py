# Generated by Django 2.0.4 on 2018-04-25 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0002_auto_20180417_0346'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='buy_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='rent_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]