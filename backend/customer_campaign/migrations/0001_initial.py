# Generated by Django 4.2.16 on 2024-11-28 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TargetCustomer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CampaignInfo',
            fields=[
                ('campaign_no', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('text', models.TextField(max_length=1500)),
                ('extra_comments', models.TextField(max_length=1055)),
                ('targetCustomer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_campaign.targetcustomer')),
            ],
        ),
    ]