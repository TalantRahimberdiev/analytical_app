# Generated by Django 4.2.16 on 2024-12-26 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_campaign', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaigninfo',
            name='targetCustomer_id',
        ),
        migrations.AddField(
            model_name='campaigninfo',
            name='customer_id',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='TargetCustomer',
        ),
    ]
