# Generated by Django 4.2.16 on 2024-12-27 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bank_tariffs', '0003_alter_loan_created_by_employee_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='created_by_employee_email',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_mymodels', to=settings.AUTH_USER_MODEL),
        ),
    ]
