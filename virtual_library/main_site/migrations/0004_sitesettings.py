# Generated by Django 2.0.4 on 2018-04-25 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0003_auto_20180425_1005'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('support', models.EmailField(default='support@example.com', max_length=254)),
                ('sales_department', models.EmailField(blank=True, max_length=254)),
                ('twilio_account_sid', models.CharField(default='ACbcad883c9c3e9d9913a715557dddff99', max_length=255)),
                ('twilio_auth_token', models.CharField(default='abd4d45dd57dd79b86dd51df2e2a6cd5', max_length=255)),
                ('twilio_phone_number', models.CharField(default='+15006660005', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
