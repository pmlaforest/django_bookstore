# Generated by Django 2.0.4 on 2018-04-26 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_shop', '0004_auto_20180426_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='session_cart',
            name='user_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
