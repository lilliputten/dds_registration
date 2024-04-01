# Generated by Django 5.0.3 on 2024-04-01 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dds_registration', '0004_remove_invoice_template'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='currency',
            field=models.TextField(choices=[('USD', 'US Dollar'), ('CHF', 'Swiss Franc'), ('EUR', 'Euro'), ('CAD', 'Canadian Dollar')], default='USD'),
        ),
    ]