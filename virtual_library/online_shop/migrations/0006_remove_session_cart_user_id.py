# Generated by Django 2.0.4 on 2018-04-26 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online_shop', '0005_session_cart_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session_cart',
            name='user_id',
        ),
    ]
