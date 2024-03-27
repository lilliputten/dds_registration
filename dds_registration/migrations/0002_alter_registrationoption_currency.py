# Generated by Django 5.0.3 on 2024-03-27 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dds_registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationoption',
            name='currency',
            field=models.TextField(choices=[('USD', 'US Dollar'), ('CHF', 'Swiss Franc'), ('EUR', 'Euro'), ('CAD', 'Canadian Dollar')], default='USD'),
        ),
    ]