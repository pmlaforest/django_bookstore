# Generated by Django 2.0.4 on 2018-04-26 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_shop', '0009_auto_20180426_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session_cart',
            name='books',
            field=models.ManyToManyField(blank=True, to='main_site.Book'),
        ),
    ]
